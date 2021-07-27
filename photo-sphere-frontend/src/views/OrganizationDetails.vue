<template>
    <el-container style="margin: 32px 0px">
        <template v-if="loading">
            <div v-loading="loading"></div>
        </template>
        <template v-else>
            <el-row type="flex">
                <el-col :span="24">
                    <el-avatar
                        fit="contain"
                        :size="160"
                        style="margin-bottom: 16px; border: 2px solid teal"
                    >
                        <img
                            :src="organization.avatar"
                            oncontextmenu="return false;"
                        />
                    </el-avatar>
                    <el-container
                        style="justify-content: center; margin-bottom: 32px"
                    >
                        <span>{{ organization.name }}</span>
                    </el-container>
                </el-col>

                <template v-if="membersLoading">
                    <div v-loading="membersLoading"></div>
                </template>
                <template v-else>
                    <el-col
                        :offset="1"
                        :span="8"
                        style="justify-content: start"
                    >
                        <el-row type="flex" align="middle">
                            <h3>Members</h3>
                            <span style="margin-right: 16px">{{
                                members.length
                            }}</span>
                            <el-button
                                size="mini"
                                icon="el-icon-circle-plus-outline"
                                @click="memberAdd = true"
                                >Add member</el-button
                            >
                        </el-row>
                        <el-descriptions :column="1" border>
                            <template v-for="(member, i) in members" :key="i">
                                <el-descriptions-item :label="member.name">
                                    {{ processRole(member.role) }}
                                </el-descriptions-item>
                            </template></el-descriptions
                        >
                    </el-col>
                </template>
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
                        @click="viewDetails(0)"
                    >
                        <el-row type="flex">
                            <el-col :span="8">
                                <img
                                    src="../../images/feature_1.jpg"
                                    class="image"
                                    oncontextmenu="return false;"
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
                        @click="viewDetails(0)"
                    >
                        <el-row type="flex">
                            <el-col :span="8">
                                <img
                                    src="../../images/feature_2.jpg"
                                    class="image"
                                    oncontextmenu="return false;"
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
        </template>
        <exhibition-create-dialog
            :dialog="exhibitionCreate"
        ></exhibition-create-dialog>
        <add-member-dialog
            v-if="organization"
            :dialog="memberAdd"
            :organization="organization.id"
            @close="memberAdd = false"
        ></add-member-dialog>
    </el-container>
</template>

<script>
import {
    getOrganizationDetails,
    getOrganizationMembers,
} from "@/api/organization.api";
import { getProfileById } from "@/api/user.api";
import AddMemberDialog from "@/components/dialog/AddMemberDialog";

export default {
    components: { AddMemberDialog },
    data() {
        return {
            id: this.$route.params.id,
            loading: false,
            organization: null,
            members: [],
            membersLoading: false,
            exhibitionCreate: false,
            memberAdd: false,
        };
    },
    methods: {
        processRole(role) {
            if (role === "A") {
                return "Admin";
            } else if (role === "E") {
                return "Editor";
            } else if (role === "M") {
                return "Moderator";
            } else {
                return "Member";
            }
        },
        viewDetails(id) {
            this.$router.push({
                name: "Exhibition-Details",
                params: { id },
            });
        },
        visitUploaderProfile() {
            this.$router.push({
                name: "User-Profile",
                params: { id: this.photo.uploader },
            });
        },
        async fetchMembers() {
            this.membersLoading = true;
            const res = await getOrganizationMembers(this.id);

            for (let i = 0; i < res.data.length; i++) {
                const user = await getProfileById(res.data[i].member);
                const member = {
                    name: user.data.first_name + " " + user.data.last_name,
                    role: res.data[i].role,
                };
                this.members.push(member);
            }
            this.membersLoading = false;
        },
    },
    created() {
        this.loading = true;

        getOrganizationDetails(this.id)
            .then((res) => {
                console.log(res);
                this.organization = res.data;
            })
            .catch((error) => console.log(error))
            .finally(() => {
                this.loading = false;
            });

        this.fetchMembers();
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