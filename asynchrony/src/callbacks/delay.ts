// simulate network delay
export function fakeDelay(ms: number, callback: () => void) {
    setTimeout(callback, ms);
}