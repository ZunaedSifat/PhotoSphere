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
                    <span>Pixels Photographic Society</span>
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
                <el-descriptions :column="1" border>
                    <template v-for="(member, i) in members" :key="i">
                        <el-descriptions-item :label="member.name">
                            {{ member.role }}
                        </el-descriptions-item>
                    </template></el-descriptions
                >
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
                <el-card
                    shadow="hover"
                    :body-style="{ padding: '0px', width: '100%' }"
                    style="margin-bottom: 8px"
                    @click="viewDetails"
                >
                    <el-row type="flex">
                        <el-col :span="8">
                            <img
                                src="../../images/feature_1.jpg"
                                class="image"
                            />
                        </el-col>
                        <el-col :span="12">
                            <div style="padding: 14px; text-align: start">
                                <h4>Focus</h4>
                                <p>23 photos</p>
                                <span>30 July - 15 August</span>
                            </div></el-col
                        >
                    </el-row>
                </el-card>
                <el-card
                    shadow="hover"
                    :body-style="{ padding: '0px', width: '100%' }"
                    @click="viewDetails"
                >
                    <el-row type="flex">
                        <el-col :span="8">
                            <img
                                src="../../images/feature_2.jpg"
                                class="image"
                            />
                        </el-col>
                        <el-col :span="12">
                            <div style="padding: 14px; text-align: start">
                                <h4>Lights Out</h4>
                                <p>44 photos</p>
                                <span>15 July - 1 August</span>
                            </div></el-col
                        >
                    </el-row>
                </el-card>
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
import { getUserPhotos } from "@/api/photo.api";

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
            members: [
                {
                    name: "Andrew NG",
                    role: "President",
                },
                {
                    name: "Christopher Yu",
                    role: "Secretary",
                },
                {
                    name: "Priyeta Saha",
                    role: "Vice President",
                },
            ],
        };
    },
    created() {
        this.photosLoading = true;
        getUserPhotos(this.id)
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

.bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.button {
    padding: 0;
    min-height: auto;
}

.image {
    width: 100%;
    height: 100%;
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