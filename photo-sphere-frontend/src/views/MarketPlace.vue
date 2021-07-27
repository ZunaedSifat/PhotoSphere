<template>
    <el-container style="margin: 32px 0px">
        <el-row type="flex">
            <el-col :offset="1" :span="8">
                <el-menu
                    @open="handleOpen"
                    @close="handleClose"
                    style="text-align: start"
                >
                    <h4>Filters</h4>
                    <el-menu-item index="1">
                        <i class="el-icon-menu"></i>
                        <span>Digital only</span>
                        <el-radio-group v-model="is_digital" size="small">
                            <el-radio-button label="true">
                                <i class="el-icon-check"></i>
                            </el-radio-button>
                            <el-radio-button label="false">
                                <i class="el-icon-close"></i>
                            </el-radio-button>
                        </el-radio-group>
                    </el-menu-item>
                    <el-menu-item index="2">
                        <i class="el-icon-time"></i>
                        <span>Uploaded after</span>

                        <el-date-picker v-model="time_low" type="date">
                        </el-date-picker>
                    </el-menu-item>
                    <el-menu-item index="3">
                        <i class="el-icon-time"></i>
                        <span>Uploaded before</span>

                        <el-date-picker
                            v-model="time_hi"
                            type="date"
                        ></el-date-picker>
                    </el-menu-item>

                    <el-submenu index="4">
                        <template #title>
                            <i class="el-icon-sort"></i>
                            <span>Order by</span>
                        </template>
                        <el-menu-item index="4-1">
                            <div>
                                <i class="el-icon-star-off"></i>
                                <span>Like Count</span>
                                <el-radio-group
                                    v-model="like_count"
                                    size="small"
                                >
                                    <el-radio-button label="true">
                                        <i class="el-icon-top"></i>
                                    </el-radio-button>
                                    <el-radio-button label="false">
                                        <i class="el-icon-bottom"></i>
                                    </el-radio-button>
                                </el-radio-group>
                            </div>
                        </el-menu-item>
                        <el-menu-item index="4-2">
                            <div>
                                <i class="el-icon-money"></i>
                                <span style="margin-right: 8px">Price</span>
                                <el-radio-group v-model="price" size="small">
                                    <el-radio-button label="New York">
                                        <i class="el-icon-top"></i>
                                    </el-radio-button>
                                    <el-radio-button label="Washington">
                                        <i class="el-icon-bottom"></i>
                                    </el-radio-button>
                                </el-radio-group>
                            </div>
                        </el-menu-item>
                    </el-submenu>
                    <el-menu-item>
                        <el-button
                            style="margin: 32px 0px; width: 50%"
                            type="primary"
                            @click="searchWithFilters"
                            >Search</el-button
                        >
                    </el-menu-item>
                </el-menu>
            </el-col>

            <el-col :offset="1" :span="13">
                <template v-if="loading">
                    <div style="margin: 32px" v-loading="loading"></div>
                </template>
                <template v-else>
                    <el-space alignment="start" size="large" wrap>
                        <el-card
                            style="text-align: start"
                            v-for="(photo, index) in photos"
                            :key="index"
                            :photo="photo"
                            shadow="hover"
                            @click="viewDetails(photo.id)"
                            :body-style="{ padding: '0px', width: '300px' }"
                        >
                            <div style="position: relative">
                                <img
                                    :src="photo.image"
                                    class="image"
                                    oncontextmenu="return false;"
                                />
                            </div>

                            <div class="bottom">
                                <div>
                                    <div
                                        style="padding: 8px; font-weight: bold"
                                    >
                                        <span>{{ photo.title }}</span>
                                    </div>

                                    <div style="padding: 8px">
                                        <span>${{ photo.price }}</span>
                                    </div>
                                </div>
                                <div
                                    style="
                                        display: inline-block;
                                        margin-right: 8px;
                                    "
                                >
                                    <el-button
                                        class="icon-button"
                                        circle
                                        style="margin-right: 8px"
                                    >
                                        <font-awesome-icon
                                            :icon="['far', 'heart']"
                                        ></font-awesome-icon>
                                    </el-button>
                                    <span class="caption">{{
                                        photo.like_count
                                    }}</span>
                                </div>
                            </div>
                        </el-card>
                    </el-space>
                </template>
            </el-col>
        </el-row>
    </el-container>
</template>

<script>
import { getFilteredPhotos } from "@/api/photo.api";

export default {
    data() {
        return {
            loading: false,
            photos: [],
            is_digital: null,
            time_low: null,
            time_hi: null,
            order_by: "",
            like_count: null,
            price: null,
        };
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        searchWithFilters() {
            var params = {
                for_sale: true,
                is_digital: this.is_digital,
            };
            if (this.time_low) {
                params["time_low"] = new Date(this.time_low).toISOString();
            }
            if (this.time_hi) {
                params["time_hi"] = new Date(this.time_hi).toISOString();
            }

            if (this.like_count != null) {
                params["order_by"] = this.like_count
                    ? "like_count"
                    : "-like_count";
            } else if (this.price != null) {
                params["price"] = this.price ? "price" : "-price";
            }
            this.loading = true;

            getFilteredPhotos(params)
                .then((res) => {
                    console.log(res);
                    this.photos = res.data;
                    console.log(this.photos);
                })
                .catch((error) => {
                    console.log(error.response);
                })
                .finally(() => setTimeout(() => (this.loading = false), 1000));
        },
        viewDetails(id) {
            this.$router.push({
                name: "Photo-Details",
                params: { id },
            });
        },
    },
    created() {
        const params = {
            for_sale: true,
        };
        this.loading = true;

        getFilteredPhotos(params)
            .then((res) => {
                this.photos = res.data;
                console.log(this.photos);
            })
            .catch((error) => {
                console.log(error.response);
            })
            .finally(() => setTimeout(() => (this.loading = false), 1000));
    },
};
</script>


<style lang="scss" scoped>
span {
    margin-right: 8px;
}

.el-menu-item:hover {
    color: $primary-color !important;
}

.bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.image {
    width: 100%;
    height: 200px;
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