<template>
    <el-container style="margin: 32px 0px">
        <template v-if="loading">
            <div v-loading="loading"></div>
        </template>
        <template v-else>
            <el-row type="flex">
                <el-col :offset="1" :span="6">
                    <el-card :body-style="{ padding: '0px' }">
                        <img
                            :src="exhibition.avatar"
                            class="image"
                            oncontextmenu="return false;"
                        />

                        <div style="padding: 14px; text-align: left">
                            <div class="bottom">
                                <h3>{{ exhibition.title }}</h3>
                                <div>
                                    <div style="display: inline-block">
                                        <el-button
                                            type="primary"
                                            icon="el-icon-document-add"
                                            style="padding: 8px 16px"
                                            @click="addEntry = true"
                                        >
                                            Submit An Entry
                                        </el-button>
                                    </div>
                                </div>
                            </div>
                            <p class="caption">
                                {{ exhibition.description }}
                            </p>
                            <template v-if="organizationLoading">
                                <div v-loading="organizationLoading"></div>
                            </template>
                            <template v-else>
                                <p style="font-size: 15px">
                                    Organized by <b>{{ organization.name }}</b>
                                </p>
                            </template>
                            <p style="font-size: 15px">
                                {{
                                    new Date(
                                        exhibition.start_date
                                    ).toDateString()
                                }}
                                -
                                {{
                                    new Date(exhibition.end_date).toDateString()
                                }}
                            </p>
                            <p style="font-size: 15px">
                                Entry Fee BDT
                                <b>{{ exhibition.entry_fee }}</b>
                            </p>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="1">
                    <el-divider direction="vertical"></el-divider>
                </el-col>
                <el-col :span="16">
                    <template v-if="photosLoading">
                        <div v-loading="photosLoading"></div>
                    </template>
                    <template v-else>
                        <el-row type="flex">
                            <el-col
                                :offset="1"
                                :span="7"
                                v-for="(photo, index) in photos"
                                :key="index"
                            >
                                <photo-preview-card
                                    :photo="photo"
                                ></photo-preview-card>
                            </el-col>
                        </el-row>

                        <!-- <el-space alignment="start" size="large" wrap>
                            <photo-preview-card
                                v-for="(photo, index) in photos"
                                :key="index"
                                :photo="photo"
                            ></photo-preview-card>
                        </el-space> -->
                    </template>
                </el-col>
            </el-row>
        </template>
        <add-entry-dialog
            v-if="exhibition"
            :dialog="addEntry"
            :exhibition="exhibition.id"
            @add="addNewEntry"
            @close="addEntry = false"
        ></add-entry-dialog>
    </el-container>
</template>

<script>
import {
    getExhibitionDetails,
    getExhibitionEntries,
} from "@/api/exhibition.api";
import { getOrganizationDetails } from "@/api/organization.api";
import { getPhotoDetails } from "@/api/photo.api";
import PhotoPreviewCard from "@/components/photo/PhotoPreviewCard";
import AddEntryDialog from "@/components/dialog/AddEntryDialog";

export default {
    components: {
        PhotoPreviewCard,
        AddEntryDialog,
    },
    data() {
        return {
            id: this.$route.params.id,
            exhibition: null,
            loading: false,
            organizationLoading: false,
            organization: null,
            addEntry: false,
            photos: [],
            photosLoading: false,
            entries: [],
        };
    },
    methods: {
        addNewEntry(entry) {
            this.entries.push(entry);
        },
        async fetchPhotos() {
            this.photosLoading = true;

            const res = await getExhibitionEntries(this.id);
            this.entries.push(...res.data);

            for (let i = 0; i < this.entries.length; i++) {
                const photoResponse = await getPhotoDetails(
                    this.entries[i].photo
                );
                this.photos.push(photoResponse.data);
            }
            this.photosLoading = false;
        },
    },
    created() {
        this.loading = true;
        this.organizationLoading = true;
        getExhibitionDetails(this.id)
            .then((res) => {
                console.log(res);
                this.exhibition = res.data;
                this.loading = false;

                getOrganizationDetails(this.exhibition.organizer).then(
                    (org) => {
                        this.organization = org.data;
                        console.log(this.organization);

                        this.organizationLoading = false;
                    }
                );

                this.fetchPhotos();
            })
            .catch((error) => {
                console.log(error);
                this.loading = false;
                this.organizationLoading = false;
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
    color: rgb(100, 100, 100);
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
