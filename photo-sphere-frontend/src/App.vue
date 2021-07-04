<template>
    <el-container>
        <el-header style="padding: 0px">
            <navbar></navbar>
        </el-header>
        <el-main>
            <router-view></router-view>
        </el-main>
        <el-footer v-if="showFooter">
            <custom-footer></custom-footer>
        </el-footer>
    </el-container>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import CustomFooter from "./components/Footer.vue";

export default {
    name: "App",
    components: {
        Navbar,
        CustomFooter,
    },
    data() {
        return {
            loading: false,
        };
    },
    computed: {
        showFooter() {
            return (
                this.$route.path != "/login" && this.$route.path != "/register"
            );
        },
    },
    methods: {
        async initializeApp() {
            this.loading = true;
            try {
                await this.$store.dispatch("auth/autoLogin");
                await this.$store.dispatch("user/fetchCurrentUserProfile");
            } catch {
                this.loading = false;
            } finally {
                this.loading = false;
            }
        },
    },
    created() {
        document.querySelector("head title").textContent = "Photo Sphere";
        console.log(this.showFooter);
        this.initializeApp();
    },
};
</script>

<style>
@font-face {
    font-family: "DIN Neuzeit Grotesk";
    src: local("DIN Neuzeit Grotesk"),
        url("../fonts/DIN Neuzeit Grotesk.ttf") format("truetype");
}

#app {
    font-family: "DIN Neuzeit Grotesk", Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

body {
    margin: 0 !important;
}

.el-footer {
    position: fixed;
    bottom: 0px;
    width: 100%;
}

.el-avatar {
    background-color: white !important;
}

.el-row {
    width: 100%;
}

.el-menu-item {
    transition: none !important;
}

.el-menu-item:hover {
    color: aqua !important;
    background: none !important;
}

.el-menu-item.is-active {
    border: none !important;
}

.el-form-item__error {
    padding-top: 6px !important;
}

i {
    margin: 0px !important;
    font-size: 16px !important;
}
</style>
