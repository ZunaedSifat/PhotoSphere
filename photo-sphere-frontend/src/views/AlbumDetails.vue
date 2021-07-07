<template>
    <el-container style="margin: 32px 0px">
        <template v-if="loading">
            <div v-loading="loading"></div>
        </template>
        <template v-else>
            <el-row type="flex">
                <el-col :offset="1" :span="12">
                    <el-card :body-style="{ padding: '0px' }">
                        <img :src="topPhoto" class="image" />

                        <div style="padding: 14px; text-align: left">
                            <div class="bottom">
                                <span>{{ album.name }}</span>
                                <div>
                                    <!-- <div
                                        style="
                                            display: inline-block;
                                            margin-right: 8px;
                                        "
                                    >
                                        <el-button
                                            class="icon-button"
                                            
                                            circle
                                        >
                                            <font-awesome-icon
                                                :icon="['far', 'heart']"
                                            ></font-awesome-icon>
                                        </el-button>
                                        <span class="caption">{{
                                            photo.like_count
                                        }}</span>
                                    </div> -->
                                    <div style="display: inline-block">
                                        <el-button class="icon-button" circle>
                                            <font-awesome-icon
                                                :icon="['fas', 'share-alt']"
                                            ></font-awesome-icon>
                                        </el-button>
                                    </div>
                                </div>
                            </div>
                            <span class="caption">
                                {{ album.description }}</span
                            >
                        </div>
                    </el-card>
                    <template v-if="photosLoading !== 0">
                        <div v-loading="photosLoading !== 0"></div>
                    </template>
                    <template v-else>
                        <el-space alignment="start" size="medium" wrap>
                            <photo-preview-card
                                v-for="(photo, index) in photos"
                                :key="index"
                                :photo="photo"
                            ></photo-preview-card>
                        </el-space>
                    </template>
                </el-col>
                <el-col :span="1">
                    <el-divider direction="vertical"></el-divider>
                </el-col>
                <el-col :span="9">
                    <el-skeleton
                        v-if="ownerLoading"
                        :rows="5"
                        animated
                    ></el-skeleton>
                    <template v-else>
                        <el-descriptions title="Details" :column="1" border>
                            <el-descriptions-item label="Owner">
                                {{ ownerName }}
                                <el-button
                                    style="padding: 8px; margin-left: 8px"
                                    @click="visitUploaderProfile"
                                    >View Profile</el-button
                                >
                            </el-descriptions-item>
                        </el-descriptions>
                    </template>
                </el-col>
            </el-row>
        </template>
    </el-container>
</template>

<script>
import { getAlbumDetails } from "@/api/album.api";
import { getProfileById } from "@/api/user.api";
import { getPhotoDetails } from "@/api/photo.api";
import PhotoPreviewCard from "@/components/photo/PhotoPreviewCard";

export default {
    components: {
        PhotoPreviewCard,
    },
    data() {
        return {
            id: this.$route.params.id,
            album: null,
            loading: false,
            ownerLoading: false,
            ownerName: null,
            topPhoto: null,
            photos: [],
            photosLoading: 100,
        };
    },
    methods: {
        visitUploaderProfile() {
            this.$router.push({
                name: "User-Profile",
                params: { id: this.album.owner },
            });
        },
    },
    created() {
        this.loading = true;
        this.ownerLoading = true;
        getAlbumDetails(this.id)
            .then((res) => {
                console.log(res);
                this.album = res.data;
                this.photosLoading = this.album.photos.length;

                getProfileById(this.album.owner).then((user) => {
                    this.ownerName =
                        user.data.first_name + " " + user.data.last_name;
                });

                getPhotoDetails(this.album.photos[0]).then((res) => {
                    this.topPhoto = res.data.image;
                    // this.photos.push(res.data);
                });

                // getPhotoDetails(this.album.photos[1]).then((res) => {

                //     this.photos.push(res.data);
                // });

                console.log("left " + this.photosLoading);
                for (let i = 0; i < this.album.photos.length; i++) {
                    getPhotoDetails(this.album.photos[i]).then(
                        (photoDetails) => {
                            this.photos.push(photoDetails);
                            console.log(photoDetails);
                            this.photosLoading--;
                            console.log("left " + this.photosLoading);
                        }
                    );
                }
            })
            .catch((error) => console.log(error))
            .finally(() => {
                this.loading = false;
                this.ownerLoading = false;
                // this.photosLoading = false;
            });
    },
};
</script>


<style lang="scss" scoped>
.el-divider--vertical {
    height: 100% !important;
}

.icon-button {
    border: none !important;
}

.caption {
    font-size: 13px;
    color: #999;
}

.bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.el-button {
    padding: 0;
    min-height: auto;
}

svg {
    font-size: 16px;
}

.image {
    width: 100%;
    display: block;
}

.el-tag {
    margin-right: 8px;
}
</style>
