import { fakeDelay } from "../callbacks/delay.ts";

// wrap callback-style async logic in a Promise

export function getWeather(city: string): Promise<string> {
    return new Promise((resolve) => {
        console.log('Fetching weather for ${city}...');
        fakeDelay(1000, () => {
            resolve('Weather in ${city}: 72F');
        });
    });
}

export function getAirQuality(city: string): Promise<string> {
    return new Promise((resolve) => {
        fakeDelay(1000, () => {
            resolve('Air quality in ${city}: Good');
        });
    });
}

export function getPollen(city: string): Promise<string> {
    return new Promise((resolve) => {
        fakeDelay(1000, () => {
            resolve('Pollen count in ${city}: Low');
        });
    });
}