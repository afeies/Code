import {
    getWeatherCallback,
    getAirQualityCallback,
    getPollenCallback,
} from "./weatherCallback.ts"

// simple single callback
getWeatherCallback("Pittsburgh", (data) => {
    console.log("Received data:", data);
});

// callback problem
// you first need to get weather, then use the weather data to get the air quality, then use both to get pollen
// callbacks don't return values, instead they fire later, so the only place you have access to their result is inside their callback
function getFullReportCallback(city: string, callback: (report: string) => void) {
    getWeatherCallback(city, (weatherData) => {
        getAirQualityCallback(city, (airQualityData) => {
            getPollenCallback(city, (pollenData) => {
                const fullReport = `${weatherData}\n${airQualityData}\n${pollenData}`;
                callback(fullReport);
            });
        });
    });
}

console.log('full report: callback problem');
getFullReportCallback("Pittsburgh", (report) => {
    console.log(report);
});