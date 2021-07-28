<template>
    <el-container style="margin: 32px 0px">
        <template v-if="loading">
            <div v-loading="loading"></div>
        </template>
        <template v-else>
            <el-row type="flex">
                <el-col :offset="1" :span="12">
                    <el-card :body-style="{ padding: '0px' }">
                        <img
                            :src="image"
                            class="image"
                            oncontextmenu="return false;"
                        />

                        <div style="padding: 14px; text-align: left">
                            <div class="bottom">
                                <span>{{ photo.title }}</span>
                                <div>
                                    <div
                                        style="
                                            display: inline-block;
                                            margin-right: 8px;
                                        "
                                    >
                                        <el-button
                                            class="icon-button"
                                            circle
                                            @click="like"
                                        >
                                            <font-awesome-icon
                                                :icon="['far', 'heart']"
                                            ></font-awesome-icon>
                                        </el-button>
                                        <span class="caption">{{
                                            like_count
                                        }}</span>
                                    </div>
                                    <div style="display: inline-block">
                                        <el-button
                                            class="icon-button"
                                            circle
                                            @click="share = true"
                                        >
                                            <font-awesome-icon
                                                :icon="['fas', 'share-alt']"
                                            ></font-awesome-icon>
                                        </el-button>
                                    </div>
                                </div>
                            </div>
                            <span class="caption"> {{ photo.caption }}</span>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="1">
                    <el-divider direction="vertical"></el-divider>
                </el-col>
                <el-col :span="9" style="text-align: left">
                    <el-skeleton
                        v-if="ownerLoading"
                        :rows="5"
                        animated
                    ></el-skeleton>
                    <template v-else>
                        <el-descriptions title="Details" :column="1" border>
                            <el-descriptions-item
                                v-if="photo.for_sale"
                                label="Price"
                            >
                                {{ photo.price }}</el-descriptions-item
                            >
                            <el-descriptions-item label="Owner">
                                {{ ownerName }}
                                <el-button
                                    style="padding: 8px; margin-left: 8px"
                                    @click="visitOwnerProfile"
                                    >View Profile</el-button
                                >
                            </el-descriptions-item>

                            <el-descriptions-item label="Tags">
                                <el-tag
                                    v-for="tag in tags"
                                    :key="tag"
                                    size="small"
                                    >{{ tag }}</el-tag
                                >
                            </el-descriptions-item>
                        </el-descriptions>
                        <h3>Preview</h3>
                        <el-row type="flex">
                            <el-col
                                v-for="(preview, index) in previews"
                                :key="index"
                                :offset="index == 0 ? 0 : 1"
                                :span="5"
                            >
                                <img :src="preview" class="preview" />
                                <div style="text-align: center">
                                    {{ 128 * Math.pow(2, index) }} x
                                    {{ 128 * Math.pow(2, index) }}
                                </div>
                            </el-col>
                        </el-row>
                        <el-button
                            type="primary"
                            style="
                                width: 100%;
                                padding: 12px 80px;
                                margin-top: 24px;
                            "
                            @click="purchase = true"
                            >PURCHASE</el-button
                        >
                    </template>
                </el-col>
            </el-row>
        </template>
        <share-photo
            v-if="photo"
            :dialog="share"
            :photoURL="photo.image"
            @close="share = false"
        ></share-photo>
        <photo-purchase-dialog
            v-if="photo"
            :dialog="purchase"
            :photo="photo.id"
            @close="purchase = false"
        ></photo-purchase-dialog>
    </el-container>
</template>

<script>
import { getPhotoDetails, likePhoto } from "@/api/photo.api";
import { getProfileById } from "@/api/user.api";
import { getTag } from "@/api/tag.api";
import SharePhoto from "@/components/photo/SharePhoto.vue";
import PhotoPurchaseDialog from "@/components/dialog/PhotoPurchaseDialog";

export default {
    components: {
        SharePhoto,
        PhotoPurchaseDialog,
    },
    data() {
        return {
            id: this.$route.params.id,
            photo: null,
            like_count: 0,
            loading: false,
            ownerLoading: false,
            ownerName: null,
            tagsLoading: false,
            tags: [],
            image: null,
            previews: [],
            share: false,
            purchase: false,
        };
    },
    methods: {
        async like() {
            await likePhoto(this.id);
            this.like_count++;
        },
        visitOwnerProfile() {
            this.$router.push({
                name: "User-Profile",
                params: { id: this.photo.owner },
            });
        },
        async fetchTags() {
            this.tagsLoading = true;
            for (let i = 0; i < this.photo.tags.length; i++) {
                const tagResponse = await getTag(this.photo.tags[i]);
                this.tags.push(tagResponse.data.name);
            }
            this.tagsLoading = false;
        },
    },
    created() {
        this.loading = true;
        this.ownerLoading = true;

        getPhotoDetails(this.id)
            .then((res) => {
                console.log(res);
                this.photo = res.data;
                this.like_count = this.photo.like_count;

                if (this.photo.owner == this.$store.state.user.id) {
                    // show original images
                    this.image = this.photo.image;
                    this.previews.push(this.photo.optimized_image_128);
                    this.previews.push(this.photo.optimized_image_256);
                    this.previews.push(this.photo.optimized_image_512);
                    this.previews.push(this.photo.optimized_image_1024);
                } else {
                    // show watermarked images
                    this.image = this.photo.watermarked_optimized_image_256;
                    this.previews.push(
                        this.photo.watermarked_optimized_image_128
                    );
                    this.previews.push(
                        this.photo.watermarked_optimized_image_256
                    );
                    this.previews.push(
                        this.photo.watermarked_optimized_image_512
                    );
                    this.previews.push(
                        this.photo.watermarked_optimized_image_1024
                    );
                }

                getProfileById(this.photo.owner).then((user) => {
                    this.ownerName =
                        user.data.first_name + " " + user.data.last_name;
                });

                this.fetchTags();
            })
            .catch((error) => console.log(error))
            .finally(() => {
                this.loading = false;
                this.ownerLoading = false;
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

.preview {
    width: 100%;
}
</style>
