<template>
    <el-container style="margin: 32px 0px">
        <el-row type="flex">
            <el-col :offset="1" :span="8">
                <el-button
                    style="margin-top: 100px"
                    icon="el-icon-circle-plus-outline"
                    type="primary"
                    @click="organizationCreate = true"
                    >Create New Organization</el-button
                >
                <h4>Start a new organization</h4>
                <h5>or</h5>
                <h4>Join an existing organization</h4>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
            <el-col :offset="1" :span="13">
                <template v-if="loading">
                    <div style="margin: 32px" v-loading="loading"></div>
                </template>
                <template v-else>
                    <el-card
                        shadow="hover"
                        body-style="text-align: left; font-size: 0.9em"
                        style="width: 90%; margin-bottom: 32px"
                        v-for="(org, index) in organizations"
                        :key="index"
                        @click="viewDetails(org.id)"
                    >
                        <template #header>
                            <el-row type="flex" align="top">
                                <el-col :span="8">
                                    <img
                                        :src="org.avatar"
                                        class="image"
                                        oncontextmenu="return false;"
                                    />
                                </el-col>
                                <el-col :span="16">
                                    <div
                                        style="
                                            padding: 0px 14px;
                                            text-align: start;
                                        "
                                    >
                                        <h4
                                            style="
                                                margin-bottom: 8px;
                                                margin-top: 4px;
                                            "
                                        >
                                            {{ org.name }}
                                        </h4>
                                        <div
                                            style="
                                                color: grey;
                                                display: -webkit-box;
                                                -webkit-line-clamp: 2;
                                                -webkit-box-orient: vertical;
                                                overflow: hidden;
                                                text-overflow: ellipsis;
                                            "
                                        >
                                            {{ org.description }}
                                        </div>
                                        <br />
                                        <div>
                                            {{ org.members.length }} members
                                        </div>
                                    </div></el-col
                                >
                            </el-row>
                        </template>
                        <el-descriptions column="1" border>
                            <el-descriptions-item label="Website">{{
                                org.website
                            }}</el-descriptions-item>
                            <el-descriptions-item label="Active since">{{
                                new Date(org.created_at).toUTCString()
                            }}</el-descriptions-item>
                        </el-descriptions>
                    </el-card>
                </template>
            </el-col>
        </el-row>
        <organization-create-dialog
            :dialog="organizationCreate"
            @create="addNewOrganization"
            @close="organizationCreate = false"
        ></organization-create-dialog>
    </el-container>
</template>

<script>
import OrganizationCreateDialog from "@/components/dialog/OrganizationCreateDialog";
import { getAllOrganizations } from "@/api/organization.api";

export default {
    components: {
        OrganizationCreateDialog,
    },
    data() {
        return {
            loading: false,
            organizationCreate: false,
            organizations: [],
        };
    },
    methods: {
        viewDetails(id) {
            this.$router.push({
                name: "Organization-Details",
                params: { id },
            });
        },
        addNewOrganization(org) {
            this.organizations.push(org);
        },
    },
    created() {
        this.loading = true;
        getAllOrganizations()
            .then((res) => {
                this.organizations = res.data;
                console.log(this.organizations);
            })
            .catch((error) => {
                console.log(error.response);
            })
            .finally(() => setTimeout(() => (this.loading = false), 1000));
    },
};
</script>


<style lang="scss" scoped>
.el-divider--vertical {
    height: 100% !important;
}

.el-avatar > img {
    width: 100%;
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