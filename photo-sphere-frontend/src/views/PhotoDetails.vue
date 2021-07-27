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
                            :src="photo.image"
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
                                        <el-button class="icon-button" circle>
                                            <font-awesome-icon
                                                :icon="['far', 'heart']"
                                            ></font-awesome-icon>
                                        </el-button>
                                        <span class="caption">{{
                                            photo.like_count
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
                <el-col :span="9">
                    <el-skeleton
                        v-if="uploaderLoading"
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
                                {{ uploaderName }}
                                <el-button
                                    style="padding: 8px; margin-left: 8px"
                                    @click="visitUploaderProfile"
                                    >View Profile</el-button
                                >
                            </el-descriptions-item>
                            <el-descriptions-item label="Uploader">
                                {{ uploaderName }}
                                <el-button
                                    style="padding: 8px; margin-left: 8px"
                                    @click="visitUploaderProfile"
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
                        <el-button
                            type="primary"
                            style="
                                width: 100%;
                                padding: 12px 80px;
                                margin-top: 24px;
                            "
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
    </el-container>
</template>

<script>
import { getPhotoDetails } from "@/api/photo.api";
import { getProfileById } from "@/api/user.api";
import { getTag } from "@/api/tag.api";
import SharePhoto from "@/components/photo/SharePhoto.vue";

export default {
    components: {
        SharePhoto,
    },
    data() {
        return {
            id: this.$route.params.id,
            photo: null,
            loading: false,
            uploaderLoading: false,
            uploaderName: null,
            tagsLoading: false,
            tags: [],
            share: false,
        };
    },
    methods: {
        visitUploaderProfile() {
            this.$router.push({
                name: "User-Profile",
                params: { id: this.photo.uploader },
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
        this.uploaderLoading = true;

        getPhotoDetails(this.id)
            .then((res) => {
                console.log(res);
                this.photo = res.data;

                getProfileById(this.photo.uploader).then((user) => {
                    this.uploaderName =
                        user.data.first_name + " " + user.data.last_name;
                });

                this.fetchTags();
            })
            .catch((error) => console.log(error))
            .finally(() => {
                this.loading = false;
                this.uploaderLoading = false;
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
