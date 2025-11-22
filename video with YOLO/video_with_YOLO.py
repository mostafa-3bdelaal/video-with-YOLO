
from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(r"C:\VS 2022\video with YOLO\When My City's Traffic Lights Turn Off __ ViralHog.mp4")

save_output = True
if save_output:
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter('track_output.avi',cv2.VideoWriter_fourcc(*'XVID'),fps,(width, height))

# ====== نافذة قابلة للتكبير/التصغير ======
cv2.namedWindow("YOLOv8 Object Tracking", cv2.WINDOW_NORMAL)

# اختياري: تقدر تحدد حجم أولي للنافذة (مش Fullscreen)
cv2.resizeWindow("YOLOv8 Object Tracking", 1280, 720)

# ================= LOOP =================
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(source=frame, persist=True, conf=0.3)

    annotated_frame = results[0].plot()

    # لو YOLO رجّع حجم مختلف → نرجعه لأبعاد الفيديو الأصلي
    if annotated_frame.shape[:2] != frame.shape[:2]:
        annotated_frame = cv2.resize(annotated_frame, (frame.shape[1], frame.shape[0]))

    cv2.imshow("YOLOv8 Object Tracking", annotated_frame)

    if save_output:
        out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if save_output:
    out.release()
cv2.destroyAllWindows()





##################################################
##################################################

# from ultralytics import YOLO
# import cv2

# # Load YOLOv8n model
# model = YOLO('yolov8n.pt')

# # Load webcam or video file
# cap = cv2.VideoCapture("Ronaldo.mp4")  

# # Optional: Save output video
# save_output = True
# if save_output:
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))     # بيجيب عرض الاطار عشان لما نحفظ الفيديو يطلع بنفس العرض الاصلي  
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # بيجيب طول الاطار عشان لما نحفظ الفيديو يطلع بنفس الكول الاصلي  
#     fps = int(cap.get(cv2.CAP_PROP_FPS))               # بيجيب كام fram ف الثانيه 
#     out = cv2.VideoWriter('tracked_output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height)) 
#     # 'tracked_output.avi'  ---> الاسم    
#     #  cv2.VideoWriter_fourcc(*'XVID')  --->  ضغط الفيديو ف الامتداد دا


# # Start video loop
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break   # لو خلص الفيديو نخرج من الحلقة

#     #  cap.read() ---> بيجيب ال صوره الحاليه ويخزنخا ف   frame
#     # ret ---> بيقولك الصوره اتخزنت ولا لا 

#     # Run detection and tracking
#     results = model.track(source=frame, persist=True, conf=0.3)
#     #track --->    اننا نيدي ل كل حاجه id     
#     # source=frame ---> ان الحاجه اللي الموديل هيقرأها هي frame     
#     #   persist=True ---> ان ال id بتاع نفس الشيئ يفضل ثلبت ف الاطارات الباقيه ميتغيرش ف كل اطار    


#     # Plot results
#     annotated_frame = results[0].plot()
#     #  .plot() --->   ترسم الصناديق (Bounding Boxes) حوالين الأجسام المكتشفة. 
#     # تضيف الـ labels (اسم الجسم أو الـ class).
#     # تضيف ID لو استخدمت track() مع persist=True.



#     # Show the frame
#     cv2.imshow("YOLOv8 Object Tracking", annotated_frame)
#     # ده بيعرض الإطار الحالي (annotated_frame) على الشاشة في نافذة جديدة باسم "YOLOv8 Object Tracking"   


#     # Save if enabled
#     if save_output:
#         out.write(annotated_frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # الرقم 1 هنا ليس وقت الانتظار قبل الإغلاق، بل مدة انتظار قصيرة للتحقق من ضغط المفتاح
#         break

# # Clean up
# cap.release()                  # غلق الفيديو الأصلي
# if save_output:   
#     out.release()              # غلق الفيديو الناتج بعد الحفظ
# cv2.destroyAllWindows()        # غلق كل نوافذ العرض المفتوحة
