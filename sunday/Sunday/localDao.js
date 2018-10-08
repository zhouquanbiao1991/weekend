.pragma library

function dbInit(){
    var db = LocalStorage.openDatabaseSync("SundaySqliteDB", "", "task_table", 1000000)
    try{
        db.transation(function (tx){
            tx.executeSql('CREATE TABLE IF NOT EXISTS task_log (time text, title text, content text)')
        })
    }catch(err)
    {
        console.log("Error: fail to creat table 'task' in db: " + err)
    }
    return db
}

function read(){

}

function add(){

}

function update(){

}

function del(){

}
