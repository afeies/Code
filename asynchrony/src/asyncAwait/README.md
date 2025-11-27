### Folder structure
- every folder (callbacks, promises, asynchAwait) contains:
1. a file that defines the async operations
    - weatherCallback.ts, weatherPromise.ts, weatherAsync.ts
2. a file that uses those operations
    - mainCallbacks.ts, mainPromises.ts, mainAsync.ts

### Reuse Promise API for async/await
- async/await requires functions that return Promises
- promises are the modern standard for defining asychronous APIs
- async/await is just syntactic sugar on top of promises

### Notes
- async/await is syntax sugar on top of promises
- when you write `await getWeather()`, JS automatically waits for the promis to resolve and returns its value, without needing .then()
- this makes asynchronous code look and feel like synchronous code
- using try/catch with async/await gives clean central error handling, just like synchronous exceptions