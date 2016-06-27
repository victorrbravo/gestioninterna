// IndexedDB implementations still use API prefixes
var indexedDB = window.indexedDB ||    // Use the standard DB API
    window.mozIndexedDB ||             // Or Firefox's early version of it
    window.webkitIndexedDB;            // Or Chrome's early version

// Firefox does not prefix these two:
var IDBTransaction = window.IDBTransaction || window.webkitIDBTransaction;
var IDBKeyRange = window.IDBKeyRange || window.webkitIDBKeyRange;

// We'll use this function to log any database errors that occur


function logerr(e) {
    console.log("IndexedDB error" + e.code + ": " + e.message);
}

// This function asynchronously obtains the database object (creating and
// initializing the database if necessary) and passes it to the function f().
function withDB(f) {
  var request = indexedDB.open("wires"); // Request the wire database
  request.onerror = logerr;                 // Log any errors
  request.onsuccess = function() {          // Or call this when done
    var db = request.result;  // The result of the request is the database
    if (db.version === "1.0") f(db);   // If db is inited, pass it to f()
    else initdb(db,f);               // Otherwise initialize it first
  }
}

function lookupWire(name, callback) {
    withDB(function(db) {
        // Create a transaction object for this query
        var transaction = db.transaction(["wires"],  // Object stores we need
                              IDBTransaction.READ_ONLY, // No updates
                                         0);            // No timeout

        // Get the object store from the transaction
        var objects = transaction.objectStore("wires");

        // Now request the object that matches the specified wires key.
        // The lines above were synchronous, but this one is async
        var request = objects.get(name);

        request.onerror = logerr;          // Log any errors that occur
        request.onsuccess = function() {   // Pass the result to this function
            // The result object is now in the request.result
            var object = request.result;
            if (object)  // If we found a match, pass city and state to callback
                callback(object.working + ", " + object.language);
            else         // Otherwise, tell the callback that we failed
                callback("Unknown name");
        }
    });
}


function saveWire(val, callbacks) {
    withDB(function(db) {
        
        var transaction = db.transaction(["wires"],  
                              IDBTransaction.READ_WRITE,
                                         0);            

        // Get the object store from the transaction
        var objects = transaction.objectStore("wires");

        // Now request the object that matches the specified wires key.
        // The lines above were synchronous, but this one is async
        var request = objects.get(val.name);

        request.onerror = logerr;          // Log any errors that occur
        request.onsuccess = function() {   // Pass the result to this function
            // The result object is now in the request.result
            var object = request.result;
            if (object)  // If we found a match, pass city and state to callback
            {

               objects.delete(val.name);
               var record = {           // This is the object we'll store
                    name: val.name,  // All properties are string
                    working: YAHOO.lang.JSON.stringify(val.working),
                    language: "editFlow"
                };
                
                objects.put(record);   // Or use add() to avoid overwriting
              callbacks.success.call(callbacks.scope, "ok");
              //  callback(object.working + ", " + object.language);
            }
            else         // Otherwise, tell the callback that we failed
            {
              
                var record = {           // This is the object we'll store
                    name: val.name,  // All properties are string
                    working: YAHOO.lang.JSON.stringify(val.working),
                    language: "editFlow"
                };
               
                     // The best part about the IndexedDB API is that object
                    // stores are *really* simple.  Here's how we add a record:
                    objects.put(record);   // Or use add() to avoid overwriting
              
              callbacks.success.call(callbacks.scope, "ok");

            }
        }
    });
}



function lookupWires(language, callback, callbacks, results) {
    withDB(function(db) {
        // As above, we create a transaction and get the object store
        var transaction = db.transaction(["wires"],
                                         IDBTransaction.READ_ONLY, 0);
        var store = transaction.objectStore("wires");
        // This time we get the city index of the object store
        var index = store.index("languages");


        var range = new IDBKeyRange.only(language);  // A range with only() one key

        // Everything above has been synchronous.
        // Now we request a cursor, which will be returned asynchronously.
        var request = index.openCursor(range);   // Request the cursor
        request.onerror = logerr;                // Log errors
        request.onsuccess = function() {         // Pass cursor to this function

            var cursor = request.result    // The cursor is in request.result
            if (!cursor)
            {
              callbacks.success.call(callbacks.scope, results);
              return;           // No cursor means no more results
            }
            var object = cursor.value      // Get the matching record
            callback(object);              // Pass it to the callback
            cursor.continue();             // Ask for the next matching record

        };
    });
}

function deleteWire(val, callbacks) {
    withDB(function(db) {
        // Create a transaction object for this query
        var transaction = db.transaction(["wires"],  // Object stores we need
                              IDBTransaction.READ_WRITE, // No updates
                                         0);            // No timeout

        // Get the object store from the transaction
        var objects = transaction.objectStore("wires");

        // Now request the object that matches the specified wires key.
        // The lines above were synchronous, but this one is async
        var request = objects.get(val.name);

        request.onerror = logerr;          // Log any errors that occur
        request.onsuccess = function() {   // Pass the result to this function
            // The result object is now in the request.result
            var object = request.result;
            if (object)  
            {
               objects.delete(val.name);
              
              callbacks.success.call(callbacks.scope, "ok");
            }
            else         
            {
                 status("Wire not found ");
            }
        }
    });
}

function prepareWires(language, results, callbacks) {
    //var output = document.getElementById("wiress");
    //output.innerHTML = "Matching wiress:";
    lookupWires(language, function(o) {
        results.push({
    				name: o.name,
    		 	working: o.working,
      		language: o.language
      	});
    }, callbacks, results);
    
}


// Set up the structure of the database and populate it with data, then pass
// the database to the function f(). withDB() calls this function if the
// database has not been initialized yet. This is the trickiest part of the
// program, so we've saved it for last.
function initdb(db, f) {
    // Downloading wires data and storing it in the database can take
    // a while the first time a user runs this application.  So we have to
    // provide notification while that is going on.
   
    function status(msg) { alert(msg.toString()); };

    status("Initializing wires database");

    // The only time you can define or alter the structure of an IndexedDB
    // database is in the onsucess handler of a setVersion request.
    var request = db.setVersion("1.0");       // Try to update the DB version
    request.onerror = status;               // Display status on fail
    request.onsuccess  = function() {       // Otherwise call this function
       
     
        var store = db.createObjectStore("wires", // store name
                                         { keyPath: "name" });

        // Now index the object store by city name as well as by zipcode.
        // With this method the key path string is passed directly as a
        // required argument rather than as part of an options object.
        store.createIndex("languages", "language");
        store.createIndex("workings", "working");        

                
//        var transaction = db.transaction(["wires"], // object stores
//                                         IDBTransaction.READ_WRITE);
//
//
//        var store = transaction.objectStore("wires");
//
//
//
//            var record = {           // This is the object we'll store
//                name: "tickets",  // All properties are string
//                working: '{"modules":[{"name":"Start Event","value":{},"config":{"position":[1,312],"xtype":"WireIt.ImageContainer"}},{"name":"End Event","value":{},"config":{"position":[1468,266],"xtype":"WireIt.ImageContainer"}},{"name":"Task","value":{"in":"none","out":"or","id":"nuevo","query":"select status from ticket","options":"new","content":"En atención"},"config":{"position":[101,285],"xtype":"WireIt.FormContainer"}},{"name":"Task","value":{"in":"none","out":"none","id":"faltaInfo","query":"select status from ticket","options":"failinfo","content":"Faltan datos"},"config":{"position":[276,147],"xtype":"WireIt.FormContainer"}},{"name":"Task","value":{"in":"none","out":"none","id":"Aceptado","query":"select status from ticket","options":"accepted","content":"En ejecución"},"config":{"position":[473,285],"xtype":"WireIt.FormContainer"}}],"wires":[{"xtype":"WireIt.BezierArrowWire","src":{"moduleId":0,"terminal":"salida"},"tgt":{"moduleId":2,"terminal":"entrada"}},{"xtype":"WireIt.BezierArrowWire","src":{"moduleId":2,"terminal":"salida"},"tgt":{"moduleId":3,"terminal":"entrada"}},{"xtype":"WireIt.BezierArrowWire","src":{"moduleId":2,"terminal":"salida"},"tgt":{"moduleId":4,"terminal":"entrada"}},{"xtype":"WireIt.BezierArrowWire","src":{"moduleId":3,"terminal":"salida"},"tgt":{"moduleId":4,"terminal":"entrada"}},{"xtype":"WireIt.BezierArrowWire","src":{"moduleId":4,"terminal":"salida"},"tgt":{"moduleId":1,"terminal":"entrada"}}],"properties":{"name":"tickets","description":"aaaaaaaaaa","token_key":"xxxxxxx","token_keysource":"sssssssss"}}',
//                language: "editFlow"
//            };

        status("Initializing wires database: loaded ");
            
    }
}




/**
 * IndexedDB Adapter
 * @class WireIt.WiringEditor.adapters.IndexedDB
 * @static 
 */
WireIt.WiringEditor.adapters.IndexedDB = {
	
	saveWiring: function(val, callbacks) {
//		var rs = this.db.execute('select * from wirings where name=? and language=?', [val.name, val.language]);

saveWire(val, callbacks);

	},
	
	deleteWiring: function(val, callbacks) {
  deleteWire(val, callbacks);
	},
	
	listWirings: function(val, callbacks) {
  
  var results = [];
		prepareWires(val.language, results, callbacks);
		
	}
	
};
