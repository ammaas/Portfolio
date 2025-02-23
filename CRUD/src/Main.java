import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

import org.bson.Document;
import org.bson.types.ObjectId;

import java.util.ArrayList;
import java.util.List;
public class AnimalShelter {

    private MongoClient client;
    private MongoDatabase database;
    private MongoCollection<Document> collection;
    // constructor to initalize the connection with MongoDB
    public AnimalShelter(String USER, String PASS, String HOST, int PORT, String DB, String COL) {
        String connectionString = "mongodb://" + USER + ":" + PASS + "@" + HOST + ":" + PORT;
        this.client = MongoClients.create(connectionString);
        this.database = this.client.getDatabase(DB);
        this.collection = this.database.getCollection(COL);
    }
    // Implement the Create in CRUD
    public void create(Document data) {
        if (data != null) {
            this.collection.insertOne(data);
        } else {
            throw new IllegalArgumentException("Nothing to save, because data parameter is empty"); // Message to inform user nothing saved
        }
    }
    // Implement the Read in CRUD
    public FindIterable<Document> read(Document query) {
        try {
            return this.collection.find(query); // Query to list records that matched search criteria
        } catch (Exception e) {
            System.out.println("No records found, please check search parameters"); // Message to inform user query failed
        }
    }
    // Implement Update in CRUD
    public long update(Document query, Document updateData) {
        try {
            UpdateResult result = this.collection.updateMany(query, new Document("$set", upateData));
            return result.getModifiedCount(); // Query to count all modified records
        } catch (Exception e) {
            System.out.println("Update was not successful, please check search parameters"); // Message to inform user update failed
            return 0;
        }
    }
    // Implement Delete in CRUD
    public long delete(Document query) {
        try {
            DeleteResult result = this.collection.deleteMany(query);
            return result.getDeletedCount(); // Query to count all deleted records
        } catch (Exception e) {
            System.out.println("Delete was not successful, please check search parameters");
            return 0;
        }
    }
}
