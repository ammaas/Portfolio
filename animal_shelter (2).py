{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8f60ecf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymongo import MongoClient\n",
    "from bson.objectid import ObjectId\n",
    "\n",
    "class AnimalShelter(object):\n",
    "\n",
    "    def __init__(self, USER='aacuser', PASS='Fisher1', HOST='nv-desktop-services.apporto.com' , PORT='30900', DB='AAC', COL='animals'):\n",
    "        # Initialize Connection\n",
    "        \n",
    "        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))  # Set username, password, host and port properties\n",
    "        self.database = self.client['%s' % (DB)]  # Set database to pull from\n",
    "        self.collection = self.database['%s' % (COL)]  #Set collection to pull from\n",
    "\n",
    "\t# Implement Create in CRUD\n",
    "    def create(self, data):\n",
    "        if data is not None:\n",
    "         \tself.database.animals.insert_one(data) # data should be in dictionary\n",
    "        else:\n",
    "            raise Exception(\"Nothing to save, because data parameter is empty\")\n",
    "\n",
    "\t# Implement Read in CRUD\n",
    "    def read(self, query):\n",
    "        try:\n",
    "            result = self.database.animals.find(query) # Query for documents in the collection\n",
    "            return result #Display result on success\n",
    "        except Exception as e:\n",
    "            return str(\"No records found, please check search parameters\") # Query failure message\n",
    "        \n",
    "    # Implement Update in CRUD\n",
    "    def update(self, query, update_data):\n",
    "        try:\n",
    "            result = self.database.animals.update_many(query, {'$set': update_data}) # Query for data to update\n",
    "            return result.update_count   # Count of modified records\n",
    "        except Exception as e:\n",
    "            return str(\"Update was not successful, please check search parameters\") # Query and update failure message\n",
    "                    \n",
    "    # Implement Delete in CRUD\n",
    "    def delete(self, query):\n",
    "        try:\n",
    "            self.database.animals.delete_many(query)  # Query for data to delete\n",
    "            return result.deleted_count   # Count of deleted records\n",
    "        except Exception as e:\n",
    "            return str(\"Delete was not successful, please check search parameters\")  # Query and delete failure message\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22cd2e27",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
