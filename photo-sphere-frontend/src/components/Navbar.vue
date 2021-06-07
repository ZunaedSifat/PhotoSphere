<template>
    <el-row type="flex" align="middle" class="nav-container">
        <el-col :span="6" style="padding: 8px">
            <img src="../../icons/logo-final.svg" alt="" />
        </el-col>
        <el-col :span="6"></el-col>
        <el-col :span="12">
            <el-row type="flex" justify="end">
                <el-menu
                    default-active=""
                    mode="horizontal"
                    background-color="inherit"
                    text-color="#fff"
                >
                    <el-menu-item index="1">
                        <span>Exhibitions</span>
                        <el-divider direction="vertical"></el-divider>
                    </el-menu-item>

                    <el-menu-item index="2">
                        <span>Marketplace</span>
                        <el-divider direction="vertical"></el-divider>
                    </el-menu-item>
                    <template v-if="logged_in">
                        <el-menu-item index="3" style="margin-right: 16px">
                            <el-avatar
                                icon="el-icon-user-solid"
                                size="small"
                            ></el-avatar>
                        </el-menu-item>
                    </template>
                    <template v-else>
                        <el-menu-item index="3">
                            <span>Login</span>
                            <el-divider direction="vertical"></el-divider>
                        </el-menu-item>
                        <el-menu-item index="4">
                            <el-button
                                size="mini"
                                round
                                style="margin-right: 16px"
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
export default {
    name: "Navbar",
    props: {
        logged_in: {
            type: Boolean,
            default: true,
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

.el-divider {
    background-color: white;
    width: 1.5px;
    height: 2em;
    margin: 0 16px;
}
</style>
