<template>
    <el-container style="margin: 32px 0px">
        <template v-if="loading">
            <div v-loading="loading"></div>
        </template>
        <template v-else>
            <el-row type="flex">
                <el-col
                    :offset="1"
                    :span="10"
                    v-for="exhibition in exhibitions"
                    :key="exhibition.id"
                >
                    <el-card
                        shadow="hover"
                        :body-style="{ padding: '0px', width: '100%' }"
                        style="margin-bottom: 8px"
                        @click="viewDetails(exhibition.id)"
                    >
                        <el-row type="flex">
                            <el-col :span="8">
                                <img
                                    :src="exhibition.avatar"
                                    class="image"
                                    oncontextmenu="return false;"
                                />
                            </el-col>
                            <el-col :span="12">
                                <div style="padding: 14px; text-align: start">
                                    <h4>{{ exhibition.title }}</h4>
                                    <p>
                                        {{
                                            new Date(
                                                exhibition.start_date
                                            ).toDateString()
                                        }}
                                        -
                                        {{
                                            new Date(
                                                exhibition.end_date
                                            ).toDateString()
                                        }}
                                    </p>
                                    <p>
                                        Entry Fee BDT
                                        <b>{{ exhibition.entry_fee }}</b>
                                    </p>
                                </div>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
                <el-col :span="1"></el-col>
            </el-row>
        </template>
    </el-container>
</template>

<script>
import { getAllExhibitions } from "@/api/exhibition.api";

export default {
    data() {
        return {
            loading: false,
            exhibitions: [],
        };
    },
    methods: {
        viewDetails(id) {
            this.$router.push({
                name: "Exhibition-Details",
                params: { id },
            });
        },
    },
    created() {
        this.loading = true;
        getAllExhibitions()
            .then((res) => {
                this.exhibitions.push(...res.data);
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