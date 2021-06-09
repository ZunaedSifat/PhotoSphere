import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import GAuth from 'vue3-google-oauth2'

import installElementPlus from './plugins/element'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from "@fortawesome/fontawesome-svg-core";
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { faGoogle, faFacebook } from "@fortawesome/free-brands-svg-icons";

library.add(faPhone);
library.add(faGoogle);
library.add(faFacebook);

const gAuthOptions = { clientId: process.env.VUE_APP_GOOGLE_OAUTH_CLIENT_ID, scope: 'profile email', prompt: 'select_account', fetch_basic_profile: true }


const app = createApp(App)
installElementPlus(app)
app
    .use(router)
    .use(store)
    .use(GAuth, gAuthOptions)
    .component("font-awesome-icon", FontAwesomeIcon)
    .mount('#app')