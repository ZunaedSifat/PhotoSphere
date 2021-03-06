import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import GAuth from 'vue3-google-oauth2'
import FacebookButton from "vue-share-buttons/src/components/FacebookButton";
import TwitterButton from "vue-share-buttons/src/components/TwitterButton";
import TumblrButton from "vue-share-buttons/src/components/TumblrButton";
import PinterestButton from "vue-share-buttons/src/components/PinterestButton";

import installElementPlus from './plugins/element'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from "@fortawesome/fontawesome-svg-core";
import { faHeart as emptyReact } from "@fortawesome/free-regular-svg-icons";
import { faPhone, faHeart, faShareAlt } from "@fortawesome/free-solid-svg-icons";
import { faGoogle, faFacebook } from "@fortawesome/free-brands-svg-icons";
library.add(emptyReact);
library.add(faPhone, faHeart, faShareAlt);
library.add(faGoogle, faFacebook);


const gAuthOptions = { clientId: process.env.VUE_APP_GOOGLE_OAUTH_CLIENT_ID, scope: 'profile email', prompt: 'select_account', fetch_basic_profile: true }


const app = createApp(App)
installElementPlus(app)
app
    .use(router)
    .use(store)
    .use(GAuth, gAuthOptions)
    .component("font-awesome-icon", FontAwesomeIcon)
    .component("facebook-button", FacebookButton)
    .component("twitter-button", TwitterButton)
    .component("tumblr-button", TumblrButton)
    .component("pinterest-button", PinterestButton)
    .mount('#app')