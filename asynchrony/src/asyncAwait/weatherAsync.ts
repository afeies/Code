import { fakeDelay } from "../callbacks/delay.ts";

export function getWeather(city: string): Promise<string> {
  return new Promise((resolve) => {
    console.log(`Fetching weather for ${city}...`);
    fakeDelay(1000, () => resolve(`Weather in ${city}: 72°F`));
  });
}

export function getAirQuality(city: string): Promise<string> {
  return new Promise((resolve) => {
    fakeDelay(1000, () => resolve(`AQI in ${city}: 40`));
  });
}

export function getPollen(city: string): Promise<string> {
  return new Promise((resolve) => {
    fakeDelay(1000, () => resolve(`Pollen in ${city}: Low`));
  });
}