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
                document.getElementById("assert_text").value = dataList.assertText;
                // window.alert(dataList.assertText)
                //console.log('请求方法：',dataList.req_method)
                if (dataList.req_method == "post"){
                    document.getElementById("post").setAttribute("checked", "")
                }
                if (dataList.req_type == "json"){
                    document.getElementById("json").setAttribute("checked", "")
                }

                //初始化菜单
                ProjectInit('project_name', 'module_name', dataList.project_name, dataList.module_name)
            }else{
                window.alert("用例的id不存在")

            }
        });
    }
    // 调用getCaseInfo函数
    getCaseInfo();

};


// 添加任务--或者用例列表
var CaseListInit = function () {

    function getCaseListInfo(){

        var options = "";
        // 获取某个用例的信息
        $.get("/interface/get_case_list", {},
            function (resp) {
            if(resp.success === "true"){
               var cases = resp.data;
               for (var i=0; i< cases.length; i++){
                   var option = '<input type="checkbox" name= "'+ cases[i].name
                         +'" value="'+ cases[i].id +'"/>' +cases[i].name + '<br>'
                   options = options + option;
               }
               var devCaseList = document.querySelector(".caseList");
               devCaseList.innerHTML = options;
               console.log("用例列表：",options);

            }else{
                window.alert(resp.message);
            }
        });
    }
    // 调用getCaseListInfo函数
    getCaseListInfo();

};

