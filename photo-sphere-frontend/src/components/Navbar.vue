<template>
    <el-row type="flex" align="middle" class="nav-container">
        <el-col :span="6" style="padding: 8px">
            <router-link to="/" exact>
                <img
                    src="../../icons/logo-final.svg"
                    alt=""
                    oncontextmenu="return false;"
                />
            </router-link>
        </el-col>
        <el-col :span="6"></el-col>
        <el-col :span="12">
            <el-row type="flex" justify="end">
                <el-menu
                    default-active=""
                    mode="horizontal"
                    router
                    background-color="inherit"
                    text-color="#fff"
                >
                    <el-menu-item index="1" route="/organizations">
                        <span>Organizations</span>
                        <el-divider direction="vertical"></el-divider>
                    </el-menu-item>
                    <el-menu-item index="2" route="/exhibitions">
                        <span>Exhibitions</span>
                        <el-divider direction="vertical"></el-divider>
                    </el-menu-item>

                    <el-menu-item index="3" route="/marketplace">
                        <span>Marketplace</span>
                        <el-divider direction="vertical"></el-divider>
                    </el-menu-item>
                    <template v-if="isLoggedIn">
                        <el-submenu
                            index="4"
                            style="margin-right: 16px; color: black"
                        >
                            <template #title>
                                <el-avatar
                                    icon="el-icon-user-solid"
                                    size="small"
                                ></el-avatar>
                            </template>

                            <el-menu-item
                                class="profile-menu"
                                index="4-1"
                                :route="profileRoute"
                                >Your profile</el-menu-item
                            >
                            <el-menu-item
                                class="profile-menu"
                                index="4-2"
                                @click="logOut"
                                >Log out</el-menu-item
                            >
                        </el-submenu>
                    </template>
                    <template v-else>
                        <el-menu-item index="3" route="/login">
                            <span>Login</span>
                            <el-divider direction="vertical"></el-divider>
                        </el-menu-item>
                        <el-menu-item index="4" route="/register">
                            <el-button size="mini" style="margin-right: 16px"
                                >REGISTER</el-button
                            >
                        </el-menu-item>
                    </template>
                </el-menu>
            </el-row>
        </el-col>
    </el-row>
</template>

<script>
import authMixin from "@/mixins/authMixin";

export default {
    name: "Navbar",
    mixins: [authMixin],
    computed: {
        profileRoute() {
            return "/user-profile/" + this.id;
        },
    },
};
</script>

<style lang="scss" scoped>
.nav-container {
    background-color: $primary-color;
}

span {
    font-size: 1.1em;
    /* font-weight: bold; */
}

.el-menu {
    border: none !important;
}

.el-menu-item {
    padding: 0px;
}

.profile-menu {
    color: darkslategrey !important;
}

.profile-menu:hover {
    color: black !important;
}

.el-divider {
    background-color: white;
    width: 1.5px;
    height: 2em;
    margin: 0 16px;
}
</style>
