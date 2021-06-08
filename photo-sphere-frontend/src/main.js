import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import installElementPlus from './plugins/element'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from "@fortawesome/fontawesome-svg-core";
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { faGoogle, faFacebook } from "@fortawesome/free-brands-svg-icons";

library.add(faPhone);
library.add(faGoogle);
library.add(faFacebook);


const app = createApp(App)
installElementPlus(app)
app
    .use(router)
    .component("font-awesome-icon", FontAwesomeIcon)
    .mount('#app')