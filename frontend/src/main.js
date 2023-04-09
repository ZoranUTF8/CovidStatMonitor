import { createApp } from "vue"; //? This imports the createApp function from the Vue library, which is used to create a new Vue application instance.
import App from "./App.vue"; //? This imports the main component of the Vue application from the App.vue file.
import router from "./router"; //? This imports the Vue router instance from the router.js file.
import "./assets/tailwind.css"; //? This imports the CSS file that provides the styling for the application.

/* 
This creates a new Vue application instance using the createApp function, passing in the main App component.
.use(router) This sets up the router instance for the Vue application instance using the use method, which registers the router with the Vue application.
.mount('#app'): This mounts the Vue application instance to the HTML element with the id of app. This renders the Vue application on the page and starts the application's lifecycle.
*/
createApp(App).use(router).mount("#app");
