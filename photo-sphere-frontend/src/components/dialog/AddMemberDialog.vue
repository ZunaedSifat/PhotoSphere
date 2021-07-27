<template>
    <el-dialog
        v-model="dialog"
        title="Add Member to Organization"
        width="40%"
        show-close
        destroy-on-close
        :before-close="onClose"
    >
        <el-form ref="form" :model="form" size="small" status-icon>
            <el-form-item label="Member" prop="member">
                <el-autocomplete
                    v-model="form.memberName"
                    ref="saveTagInput"
                    :fetch-suggestions="searchUser"
                    @select="handleSelect"
                >
                </el-autocomplete>
            </el-form-item>

            <el-form-item label="Role" prop="role">
                <el-radio-group v-model="form.role">
                    <el-radio label="A">Admin</el-radio>
                    <el-radio label="E">Editor</el-radio>
                    <el-radio label="M">Moderator</el-radio>
                </el-radio-group>
            </el-form-item>

            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 24px 16px"
                    :loading="loading"
                    @click="onCreate"
                    >ADD MEMBER
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { searchProfile } from "@/api/user.api";
import { createOrganizationMember } from "@/api/organization.api";

export default {
    name: "Add member",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        organization: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            loading: false,
            form: {
                member: "",
                memberName: "",
                role: "",
            },
        };
    },
    methods: {
        onClose(done) {
            this.$emit("close");
            done();
        },
        async searchUser(queryString, cb) {
            var results = await searchProfile(queryString);

            // call callback function to return suggestions
            var res = results.data.map((result) => {
                var fullname = result.first_name + " " + result.last_name;
                return { value: fullname, id: result.id };
            });
            console.log(res);
            cb(res);
        },
        handleSelect(user) {
            this.form.member = user.id;
        },
        async onCreate() {
            this.loading = true;
            try {
                const data = {
                    organization: this.organization,
                    member: this.form.member,
                    role: this.form.role,
                };

                const response = await createOrganizationMember(data);
                console.log(response);
                this.$emit("add", {
                    name: this.form.memberName,
                    role: this.form.role,
                });
            } catch (error) {
                console.log(error.response);
            } finally {
                this.loading = false;
                this.$emit("close");
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.el-form-item {
    text-align: start;
}

.el-tag + .el-tag {
    margin-left: 10px;
}
.button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
}
</style>