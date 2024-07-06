function createCalendarEvent() {
    // let ccalendar = CalendarApp.getCalendarById('phylosopherhossain2022@gmail.com') ;
    let sheet = SpreadsheetApp.getActiveSheet() ;
  
    let schedule = sheet.getDataRange().getValues() ;
    schedule.splice(0,1) ;
  
    var cnt = 2 ;
  
    schedule.forEach(function (entry) {
      if (entry[3] == "P") {
        ccalendar.createEvent(entry[0] , entry[1] , entry[2]) ;
        // console.log("D"+cnt)
        sheet.getRange("D"+cnt).setValue("Done") ;
      }
      cnt ++ ;
    }) ;
  }
  