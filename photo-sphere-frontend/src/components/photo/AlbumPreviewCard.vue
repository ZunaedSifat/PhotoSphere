
<template>
    <el-card
        v-if="photoPath"
        shadow="hover"
        :body-style="{ padding: '0px', width: '200px' }"
        @click="viewDetails"
    >
        <img :src="photoPath" class="image" oncontextmenu="return false;" />
        <div style="padding: 14px">
            <span>{{ album.name }}</span>
        </div>
    </el-card>
</template>

<script>
import { getPhotoDetails } from "@/api/photo.api";

export default {
    props: {
        album: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            photoPath: null,
        };
    },
    methods: {
        viewDetails() {
            this.$router.push({
                name: "Album-Details",
                params: { id: this.album.id },
            });
        },
    },
    created() {
        getPhotoDetails(this.album.photos[0]).then((res) => {
            this.photoPath = res.data.image;
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

.el-card:hover {
    cursor: pointer;
}

.el-card.is-hover-shadow:hover,
.el-card.is-hover-shadow:focus {
    box-shadow: 4px 4px 12px 0 rgb(0 0 0 / 20%);
}
</style>
