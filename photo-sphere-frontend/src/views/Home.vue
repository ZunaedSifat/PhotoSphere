<template>
    <el-container direction="vertical" style="margin: 5% 0px">
        <el-row style="width: 100%">
            <el-col :span="1"></el-col>
            <el-col :span="22">
                <el-carousel :interval="4000" type="card" arrow="always">
                    <el-carousel-item key="1">
                        <img
                            class="carousel__image"
                            src="../../images/feature_1.jpg"
                        />
                    </el-carousel-item>
                    <el-carousel-item key="2">
                        <img
                            class="carousel__image"
                            src="../../images/feature_2.jpg"
                        />
                    </el-carousel-item>
                    <el-carousel-item key="3">
                        <img
                            class="carousel__image"
                            src="../../images/feature_3.jpg"
                        />
                    </el-carousel-item>
                    <!-- <el-carousel-item v-for="item in 6" :key="item">
                        <h3 class="medium">{{ item }}</h3>
                    </el-carousel-item> -->
                </el-carousel>
            </el-col>
            <el-col :span="1"></el-col>
        </el-row>
        <h3>FEATURED PHOTOS</h3>
    </el-container>
</template>

<script>
// @ is an alias to /src

export default {
    name: "Home",
    components: {},
};
</script>

<style lang="scss" scoped>
.carousel__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>