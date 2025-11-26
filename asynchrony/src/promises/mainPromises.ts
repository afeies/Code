import {getWeather, getAirQuality, getPollen} from "./weatherPromises.ts";


// getWeather("Pittsburgh") returns a promise that will eventually contain the weather data
// when you call .then((weather) => { ... }), you are telling JS
    // when that promise resolves, run this function with the resolved weather value
getWeather("Pittsburgh")
    .then((weather) => {
        console.log("Got weather:", weather);
        return getAirQuality("Pittsburgh");
    })
    .then((aq) => {
        console.log("Got AQ:", aq);
        return getPollen("Pittsburgh");
    })
    .then((pollen) => {
        console.log("Got pollen:", pollen);
        console.log("All tasks finished!");
    });