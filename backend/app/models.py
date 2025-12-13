from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Coupon(models.Model):
    category = models.ForeignKey(Category, related_name='coupons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_value = models.DecimalField(max_digits=6, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
    

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    age = models.CharField(max_length=30, blank=True)
    pets = models.CharField(max_length=200, blank=True)
    family_info = models.TextField(max_length=1000, blank=True)
    email = models.TextField(max_length = 2000, blank=True)
    phone_number = models.TextField(max_length = 2000, blank=True)
    additional_info = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.user.username
    
class IncidentLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='incident_logs')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)  # Remove unique=True
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    transcription = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Incident Log {self.uuid} for {self.user}"

    class Meta:
        ordering = ['-timestamp']



# class Shelter(models.Model):
#     Shelter_ID = models.PositiveIntegerField(primary_key=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     phone_number = models.IntegerField(default=0)
#     email = models.CharField(max_length=30, blank=True) # EmailField for email addresses
#     website = models.URLField(max_length=200, blank=True)  # URLField for website URLs

#     def __str__(self):
#         return (self.first_name + " "+ self.last_name)

# class Recording(models.Model):
#     Recording_ID = models.PositiveIntegerField(primary_key=True)
#     audioSegment_number = models.IntegerField(default=0)
#     videdoSegment_number = models.IntegerField(default=0)
#     recording_date = models.DateField() #save location on here but create path to native storage on phone
#     audio_duration = models.DateTimeField()
#     video_duration = models.DateTimeField()
#     audioFile_size = models.FloatField()
#     videoFile_size = models.FloatField()
    
#     def __str__(self):
#         return f"Recording ID: {self.Recording_ID}"

# for audio recording 

# @Override
#     public void onClick(View arg0) {

#            SQLiteDatabase myDb;       
#            String MySQL;
#            byte[] byteImage1 = null; 
#            byte[] byteImage2 = null;
#            MySQL="create table emp1(_id INTEGER primary key autoincrement, sample TEXT not null, picture BLOB);";
#            myDb = openOrCreateDatabase("Blob List", Context.MODE_PRIVATE, null);
#            myDb.execSQL(MySQL);
#            String s=myDb.getPath();
#            textView.append("\r\n" + s+"\r\n");       
#            myDb.execSQL("delete from emp1");
#            ContentValues newValues = new ContentValues();
#            newValues.put("sample", "HI Hello");

#  try
#         {
#         FileInputStream instream = new FileInputStream("/sdcard/AudioRecorder/AudioRecorder.wav"); 
#         BufferedInputStream bif = new BufferedInputStream(instream); 
#         byteImage1 = new byte[bif.available()]; 
#         bif.read(byteImage1); 
#         textView.append("\r\n" + byteImage1.length+"\r\n"); 
#         newValues.put("picture", byteImage1); 

#         long ret = myDb.insert("emp1", null, newValues); 
#         if(ret<0) textView.append("\r\n!!! Error add blob filed!!!\r\n");
#         } catch (IOException e) 
#         {
#             textView.append("\r\n!!! Error: " + e+"!!!\r\n");   
#         }


#         Cursor cur = myDb.query("emp1",null, null, null, null, null, null);
#         cur.moveToFirst();
#         while (cur.isAfterLast() == false)
#         {
#             textView.append("\r\n" + cur.getString(1)+"\r\n");
#             cur.moveToNext();
#         }
    
#         cur.moveToFirst();
#         byteImage2=cur.getBlob(cur.getColumnIndex("picture")); 
#         bmImage.setImageBitmap(BitmapFactory.decodeByteArray(byteImage2, 0, byteImage2.length));
#         textView.append("\r\n" + byteImage2.length+"\r\n"); 

#         cur.close();
