<template>
    <el-row type="flex" align="middle" style="background-color: #6eb4ac80">
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
                        <el-menu-item index="3">
                            <el-avatar
                                style="margin-right: 16px"
                                size="small"
                                src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
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

<style scoped>
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
    background-color: darkgrey;
    width: 1.5px;
    height: 2em;
    margin: 0 16px;
}
</style>
