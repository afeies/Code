import { fakeDelay } from "./delay.ts";

// asyncronous function using a callback (like old JS APIs)
// mirrors the getBeef, cookBeef, getBuns callback examples
export function getWeatherCallback(city: string, callback: (data: string) => void) {
    console.log('Fetching weather for ${city}...');
    fakeDelay(1000, () => {callback('Weather in ${city}: 72F')});
}

export function getAirQualityCallback(city: string, callback: (data: string) => void) {
    console.log('Fetching air quality for ${city}...');
    fakeDelay(1000, () => {callback('Air quality in ${city}: Good')});
}

export function getPollenCallback(city: string, callback: (data: string) => void) {
    console.log('Fetching pollen count for ${city}...');
    fakeDelay(1000, () => {callback('Pollen count in ${city}: Low')});
}