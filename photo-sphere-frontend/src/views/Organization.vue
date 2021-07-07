<template>
    <el-container style="margin: 32px 0px">
        <el-row type="flex">
            <el-col :span="24">
                <el-avatar
                    fit="contain"
                    :size="160"
                    style="margin-bottom: 16px; border: 2px solid teal"
                >
                    <img src="../../images/organization.webp" />
                </el-avatar>
                <el-container
                    style="justify-content: center; margin-bottom: 32px"
                >
                    <span>{{ getFullName }}</span>
                </el-container>
            </el-col>

            <el-col :offset="1" :span="8" style="justify-content: start">
                <el-row type="flex" align="middle">
                    <h3>Members</h3>
                    <span style="margin-right: 16px">13</span>
                    <el-button
                        size="mini"
                        icon="el-icon-circle-plus-outline"
                        @click="photoUpload = true"
                        @close="photoUpload = false"
                        >Add member</el-button
                    >
                </el-row>

                <template v-if="photosLoading">
                    <div v-loading="photosLoading"></div>
                </template>
                <template v-else>
                    <el-space alignment="start" size="medium" wrap>
                        <photo-preview-card
                            v-for="i in grid"
                            :key="i"
                            :photo="photos[i]"
                        ></photo-preview-card>
                    </el-space>
                </template>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
            <el-col :span="14">
                <el-row type="flex" align="middle">
                    <h3>Ongoing Exhibitions</h3>
                    <el-button
                        size="mini"
                        icon="el-icon-circle-plus-outline"
                        @click="exhibitionCreate = true"
                        @close="exhibitionCreate = false"
                        >Create new exhibition</el-button
                    >
                </el-row>
            </el-col>
        </el-row>
        <exhibition-create-dialog
            :dialog="exhibitionCreate"
        ></exhibition-create-dialog>
    </el-container>
</template>

<script>
import authMixin from "@/mixins/authMixin";
import PhotoUploadDialog from "@/components/dialog/PhotoUploadDialog";
import ExhibitionCreateDialog from "@/components/dialog/ExhibitionCreateDialog";
import PhotoPreviewCard from "@/components/photo/PhotoPreviewCard";
import { getOwnPhotos } from "@/api/photo.api";

export default {
    mixins: [authMixin],
    components: {
        PhotoUploadDialog,
        ExhibitionCreateDialog,
        PhotoPreviewCard,
    },
    data() {
        return {
            grid: [],
            photoUpload: false,
            exhibitionCreate: false,
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

.el-avatar > img {
    width: 100%;
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