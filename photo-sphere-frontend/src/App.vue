<template>
    <el-container>
        <el-header style="padding: 0px">
            <navbar></navbar>
        </el-header>
        <el-main>
            <!-- <router-view></router-view> -->
        </el-main>
    </el-container>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
    name: "App",
    components: {
        Navbar,
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
</style>
