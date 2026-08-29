// 1. Clear every single running interval and timeout loop
let id = window.setTimeout(function() {}, 0);
while (id--) { window.clearTimeout(id); window.clearInterval(id); }

// 2. Clear all event listeners by cloning and replacing the body
let oldBody = document.body;
let newBody = oldBody.cloneNode(true);
oldBody.parentNode.replaceChild(newBody, oldBody);

console.log("All active scripts, timers, and events nuked!");

