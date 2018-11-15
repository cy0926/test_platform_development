// 获取指定case_id的用例信息
var CaseInit = function (case_id) {
    var dataList = [];


    function getCaseInfo(){
        // 获取某个用例的信息
        $.post("/interface/get_case_info/", {"caseId":case_id},
            function (resp) {
            if(resp.success === "true"){
                dataList = resp.data;
                //console.log(dataList)
                //console.log(dataList.name)
                document.getElementById("req_name").value = dataList.name;
                document.getElementById("req_url").value = dataList.url;
                document.getElementById("req_header").value = dataList.req_header;
                document.getElementById("req_parameter").value = dataList.req_parameter;
                //console.log('请求方法：',dataList.req_method)
                if (dataList.req_method == "post"){
                    document.getElementById("post").setAttribute("checked", "")
                }

            }else{
                window.alert("用例的id不存在")
            }
        });
    }
    // 调用getCaseInfo函数
    getCaseInfo();

}
