// edit
function edit() {
    console.log('hey');
    $("li").find("button").on("click", function() {
        var id = this.parentNode.id;
        console.log(id);
        // var status = this.checked ? 1 : 0;
        // var text = this.parentNode.text;
        // $.ajax({
        //     url: "/edit",
        //     type: "POST",
        //     data: JSON.stringify({"id": id, "status": status}),
        //     contentType: "application/json; charset=utf-8",
        //     dataType: "html",
        //     timeout: 2000,
        //     success: function() {
        //         reloadList();
        //         clearErrorBox();
        //         console.log("Successfully update item: " + id);
        //     },
        //     error: function(e, msg, type) {
        //         message = "Failed to update item '"+id+"': "+msg
        //         addError(message)
        //         console.log(message);
        //     }
        // })
    });
}

// delete
$(function() {
  $("li > .delete").on("click", function() {
    var id = this.parentNode.id;
    console.log(id);
    $.ajax({
        url: id + "/delete/",
        type: "POST",
        data: JSON.stringify({"id": id}),
        contentType: "application/json; charset=utf-8",
        dataType: "html",
        timeout: 2000,
        success: function() {
            $('#' + id).remove();
            console.log("Successfully deleted item: " + id);
        },
        error: function(e, msg, type) {
            message = "Failed to update item '"+id+"': "+msg
            console.log(message);
        }
    })
  });
});

// edit
$(function() {
  $("li > .edit").on("click", function() {
    var id = this.parentNode.id;
    console.log(id);
    $(this).hide();
    $("#" + id + " > .save").show();
    $("#" + id + " > .cancel").show();
    $("#" + id + " > .delete").hide();
    $(this.parentNode).find("input").prop("disabled", false);
  });
});

// save
$(function() {
  $("li > .save").on("click", function() {
    var id = this.parentNode.id;
    var qu_text = $(this.parentNode).find("input").val();
    $("#" + id + " > .cancel").hide();
    $("#" + id + " > .save").hide();
    $("#" + id + " > .delete").show();
    $("#" + id + " > .edit").show();
    $(this.parentNode).find("input").attr("value", qu_text);
    $(this.parentNode).find("input").prop("disabled", true);
    $.ajax({
        url: id + "/update/",
        type: "POST",
        data: JSON.stringify({"qu_text": qu_text}),
        contentType: "application/json; charset=utf-8",
        dataType: "html",
        timeout: 2000,
        success: function() {
            console.log("Successfully saved item: " + id);
        },
        error: function(e, msg, type) {
            message = "Failed to update item '"+id+"': "+msg
            console.log(message);
        }
    })
  });
});

// cancel
$(function() {
  $("li > .cancel").on("click", function() {
    var id = this.parentNode.id;
    console.log("cancel");
    $("#" + id + " > .save").hide();
    $(this).hide();
    $("#" + id + " > .delete").show();
    $("#" + id + " > .edit").show();
    $(this.parentNode).find("input").val($(this.parentNode).find("input").prop("defaultValue"));
    $(this.parentNode).find("input").prop("disabled", true);
  });
});

// function delete() {
//     $("li").find("button").on("click", function() {
//         var id = this.parentNode.id;
//         console.log(id);
//         var status = this.checked ? 1 : 0;
//         // var text = this.parentNode.text;
//         // $.ajax({
//         //     url: "/edit",
//         //     type: "POST",
//         //     data: JSON.stringify({"id": id, "status": status}),
//         //     contentType: "application/json; charset=utf-8",
//         //     dataType: "html",
//         //     timeout: 2000,
//         //     success: function() {
//         //         reloadList();
//         //         clearErrorBox();
//         //         console.log("Successfully update item: " + id);
//         //     },
//         //     error: function(e, msg, type) {
//         //         message = "Failed to update item '"+id+"': "+msg
//         //         addError(message)
//         //         console.log(message);
//         //     }
//         // })
//     });
// }