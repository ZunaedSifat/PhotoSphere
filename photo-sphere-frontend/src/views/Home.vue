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
                            oncontextmenu="return false;"
                        />
                    </el-carousel-item>
                    <el-carousel-item key="2">
                        <img
                            class="carousel__image"
                            src="../../images/feature_2.jpg"
                            oncontextmenu="return false;"
                        />
                    </el-carousel-item>
                    <el-carousel-item key="3">
                        <img
                            class="carousel__image"
                            src="../../images/feature_3.jpg"
                            oncontextmenu="return false;"
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
        <div style="text-align: left; padding: 0px 32px">
            <h3>Most Liked Photos</h3>
            <el-row type="flex">
                <el-col
                    :offset="index == 0 ? 0 : 1"
                    :span="5"
                    v-for="(photo, index) in photos"
                    :key="index"
                >
                    <el-card
                        shadow="always"
                        @click="viewPhotoDetails(photo.id)"
                    >
                        <img
                            :src="photo.image"
                            class="image"
                            oncontextmenu="return false;"
                        />
                        <div style="padding: 8px 0px">
                            {{ photo.title }}
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </el-container>
</template>

<script>
import { getMostLikedPhotos } from "@/api/photo.api";
import PhotoPreviewCard from "@/components/photo/PhotoPreviewCard.vue";

export default {
    name: "Home",
    components: { PhotoPreviewCard },
    data() {
        return {
            loading: false,
            photos: [],
        };
    },
    methods: {
        viewPhotoDetails(id) {
            this.$router.push({
                name: "Photo-Details",
                params: { id },
            });
        },
    },
    created() {
        this.loading = true;
        getMostLikedPhotos()
            .then((res) => {
                this.photos.push(...res.data);
                this.photos.splice(4);
                this.loading = false;
            })
            .catch((error) => {
                console.log(error);
                this.loading = false;
            });
    },
};
</script>

<style lang="scss" scoped>
.image {
    width: 100%;
    height: 120px;
    display: block;
}

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

.el-card:hover {
    cursor: pointer;
}
</style>