<template>
    <el-row
        type="flex"
        align="middle"
        class="footer-container"
        style="height: 100%"
    >
        <el-col :offset="7" :span="2"> About Us </el-col>
        <el-col :offset="2" :span="2"> Newsletter </el-col>
        <el-col :offset="2" :span="2"> Contact </el-col>
    </el-row>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.footer-container {
    background-color: $secondary-color;
}
</style>