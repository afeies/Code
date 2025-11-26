# Promises
- promises convert callbacks to delayed results
    - callback: a function to run later
    - promise: a value that will exist later
- analogy
    - callback: call me when the pizza is ready
    - promise: here is a pizza ticket, redeem it when ready

## Problems with callbacks
1. you don't get a value, you only get a function to run later
2. you cannot compose callbacks cleanly

## What promises fix
- I will eventually give you the result, use .then() to get it
    - will later be filled
- So, a promise replaces "pass a function" with "return an object that eventually contains a value

## Promise constructor
- `new Promise((resolve, reject) => {})`
    - can pass in both, only one, or neither
    - but best to at least include resolve
    - pass in what you plan to use

### Resolve
- changes promise state from "pending" to "fulfilled"
- stores the provided value inside the promise
- triggers any .then() callbacks waiting on it

### Reject
- mark a promise as failed
- store the error reason
- trigger any .catch() callbacks

### .then()
- `promise.then(result => {console.log(result);});`
- when this promise resolves, run this function with the solved value