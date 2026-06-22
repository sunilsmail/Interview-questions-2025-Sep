const InMemoryDBInterface = require('./InMemoryDBInterface');

class InMemoryDB extends InMemoryDBInterface {
    constructor() {
        super();

        this.records = new Map();      // key -> Map(field, value)
        this.modCount = new Map();     // key -> modifications
        this.locks = new Map();        // key -> callerId
        this.deletedLockedKeys = new Set();
    }

    incrementModifications(key) {
        this.modCount.set(
            key,
            (this.modCount.get(key) || 0) + 1
        );
    }

    setOrInc(key, field, value) {
        if (this.locks.has(key)) {
            const record = this.records.get(key);

            if (!record || !record.has(field)) {
                return null;
            }

            return record.get(field);
        }

        if (!this.records.has(key)) {
            this.records.set(key, new Map());
        }

        const record = this.records.get(key);

        record.set(
            field,
            (record.get(field) || 0) + value
        );

        this.incrementModifications(key);

        return record.get(field);
    }

    get(key, field) {
        if (!this.records.has(key)) {
            return null;
        }

        const record = this.records.get(key);

        return record.has(field)
            ? record.get(field)
            : null;
    }

    delete(key, field) {
        if (this.locks.has(key)) {
            return false;
        }

        if (!this.records.has(key)) {
            return false;
        }

        const record = this.records.get(key);

        if (!record.has(field)) {
            return false;
        }

        record.delete(field);

        this.incrementModifications(key);

        if (record.size === 0) {
            this.records.delete(key);
            this.modCount.delete(key);
        }

        return true;
    }

    topNKeys(n) {
        return [...this.modCount.entries()]
            .sort((a, b) => {
                if (b[1] !== a[1]) {
                    return b[1] - a[1];
                }

                return a[0].localeCompare(b[0]);
            })
            .slice(0, n)
            .map(([key, count]) => `${key}(${count})`);
    }

    setOrIncByCaller(key, field, value, callerId) {
        if (
            this.locks.has(key) &&
            this.locks.get(key) !== callerId
        ) {
            const record = this.records.get(key);

            if (!record || !record.has(field)) {
                return null;
            }

            return record.get(field);
        }

        if (!this.records.has(key)) {
            this.records.set(key, new Map());
        }

        const record = this.records.get(key);

        record.set(
            field,
            (record.get(field) || 0) + value
        );

        this.incrementModifications(key);

        return record.get(field);
    }

    deleteByCaller(key, field, callerId) {
        if (!this.records.has(key)) {
            return false;
        }

        if (
            this.locks.has(key) &&
            this.locks.get(key) !== callerId
        ) {
            return false;
        }

        const record = this.records.get(key);

        if (!record.has(field)) {
            return false;
        }

        record.delete(field);

        this.incrementModifications(key);

        if (record.size === 0) {
            this.records.delete(key);
            this.modCount.delete(key);

            if (this.locks.has(key)) {
                this.deletedLockedKeys.add(key);
            }
        }

        return true;
    }

    lock(callerId, key) {
        if (
            !this.records.has(key) &&
            !this.deletedLockedKeys.has(key)
        ) {
            return "invalid_request";
        }

        if (!this.locks.has(key)) {
            this.locks.set(key, callerId);
            return "acquired";
        }

        if (this.locks.get(key) === callerId) {
            return null;
        }

        return "already_locked";
    }

    unlock(key) {
        if (this.locks.has(key)) {
            this.locks.delete(key);
            this.deletedLockedKeys.delete(key);
            return "released";
        }

        if (this.records.has(key)) {
            return null;
        }

        return "invalid_request";
    }
}

module.exports = InMemoryDB;
