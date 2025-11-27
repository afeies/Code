import {getWeather, getAirQuality, getPollen} from "./weatherAsync.ts";

async function buildReport() {
    try {
        const weather = await getWeather("Pittsburgh");
        console.log("Got weather:", weather);

        const aq = await getAirQuality("Pittsburgh");
        console.log("Got AQ:", aq);

        const pollen = await getPollen("Pittsburgh");
        console.log("Got pollen:", pollen);
    } catch (err) {
        console.error("Something went wrong:", err);
    }
}

buildReport();