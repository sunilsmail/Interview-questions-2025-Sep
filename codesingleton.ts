'use strict';

import * as fs from 'fs';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let currentLine: number = 0;
let inputStringArr: string[] = [];

process.stdin.on('data', function (inputStdin: string) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputStringArr = inputString.trim().split('\n');
    main();
});

function readLine(): string {
    return inputStringArr[currentLine++];
}

/* Complete the class 'NotificationManager' below */

class NotificationManager {
    private static instance: NotificationManager;
    public notifications: { user: string; message: string }[];

    private constructor() {
        this.notifications = [];
    }

    static getInstance(): NotificationManager {
        if (!NotificationManager.instance) {
            NotificationManager.instance = new NotificationManager();
        }
        return NotificationManager.instance;
    }

    addNotification(user: string, message: string): void {
        this.notifications.push({ user, message });
    }
}

function main(): void {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const num = parseInt(readLine());
    const notificationManager1 = NotificationManager.getInstance();

    for (let i = 0; i < num; i++) {
        const user = readLine();
        const message = readLine();
        notificationManager1.addNotification(user, message);
    }

    notificationManager1.notifications.forEach(notification => {
        ws.write(`To: ${notification.user}, Message: ${notification.message}\n`);
    });

    ws.end();
}
