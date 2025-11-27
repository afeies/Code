import {getWeather, getAirQuality, getPollen} from "./weatherAsync.ts";

async function demo() {
    const [weather, aq, pollen] = await Promise.all([
        getWeather("Pittsburgh"),
        getAirQuality("Pittsburgh"),
        getPollen("Pittsburgh")
    ]);

    console.log("Got weather:", weather);
    console.log("Got AQ:", aq);
    console.log("Got pollen:", pollen);
}

demo();