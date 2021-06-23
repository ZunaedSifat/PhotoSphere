<template>
    <el-container style="margin: 32px 0px">
        <el-row type="flex">
            <el-col :span="6">
                <el-avatar fit="fill" :size="160" style="margin: 16px 0px">
                    <img src="../../images/profile.jpg" />
                </el-avatar>
                <el-container style="justify-content: center">
                    <span>{{ getFullName }}</span>
                </el-container>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
            <el-col :span="12" style="justify-content: start">
                <el-row type="flex" align="middle">
                    <h3>Photos</h3>
                    <el-button
                        size="mini"
                        icon="el-icon-upload2"
                        @click="photoUpload = true"
                        @close="photoUpload = false"
                        >Upload new photo</el-button
                    >
                </el-row>

                <template v-if="photosLoading">
                    <div v-loading="photosLoading"></div>
                </template>
                <template v-else>
                    <!-- <el-row style="margin-bottom: 16px">
                        <el-col
                            :span="7"
                            :offset="i == 0 ? 0 : 1"
                            v-for="i in grid"
                            :key="i"
                        >
                            <photo-preview-card
                                :photo="photos[i]"
                            ></photo-preview-card>
                        </el-col>
                    </el-row> -->
                    <el-space alignment="start" size="medium" wrap>
                        <photo-preview-card
                            v-for="i in grid"
                            :key="i"
                            :photo="photos[i]"
                        ></photo-preview-card>
                    </el-space>
                    <!-- <photo-preview-card
                        v-for="(photo, index) in photos"
                        :key="index"
                        :photo="photo"
                    ></photo-preview-card> -->
                </template>

                <el-row type="flex" align="middle">
                    <h3>Albums</h3>
                    <el-button size="mini" icon="el-icon-folder-add"
                        >Create new album</el-button
                    >
                </el-row>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
        </el-row>
        <photo-upload-dialog :dialog="photoUpload"></photo-upload-dialog>
    </el-container>
</template>

<script>
import authMixin from "@/mixins/authMixin";
import PhotoUploadDialog from "@/components/dialog/PhotoUploadDialog";
import PhotoPreviewCard from "@/components/photo/PhotoPreviewCard";
import { getOwnPhotos } from "@/api/photo.api";

export default {
    mixins: [authMixin],
    components: {
        PhotoUploadDialog,
        PhotoPreviewCard,
    },
    data() {
        return {
            grid: [0, 1, 2],
            photoUpload: false,
            photosLoading: false,
            photos: [],
        };
    },
    created() {
        this.photosLoading = true;
        getOwnPhotos(this.id)
            .then((res) => {
                console.log(res);
                this.photos = res.data;
                this.grid = [];
                for (var i = 0; i < this.photos.length; i++) {
                    this.grid.push(i);
                }
            })
            .catch((error) => console.log(error))
            .finally(() => (this.photosLoading = false));
    },
};
</script>

<style lang="scss" scoped>
.el-divider--vertical {
    height: 20em !important;
}

h3 {
    text-align: start;
    margin-right: 16px;
}

// .el-button {
//     padding: 8px !important;
//     height: 32px !important;
// }
</style>