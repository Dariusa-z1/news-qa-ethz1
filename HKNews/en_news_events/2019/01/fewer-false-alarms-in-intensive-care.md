# fewer-false-alarms-in-intensive-care

**Source:** en_news_events/2019/01/fewer-false-alarms-in-intensive-care.html

## Combining data

Beep, beep, beep. In intensive care units (ICU), some monitoring device or other is always sounding the alarm. Whether it’s a patient whose blood oxygen level is too low, someone in the next bed whose intracranial pressure is rising, or someone else whose blood pressure has taken a nosedive. Or perhaps just because a patient has shifted position in bed.

False alarms like this last are all too common. They utilize medical personnel’s valuable time and increase the risk that real alarms are lost in the flood of false ones. That means it is in the nurses’ and doctors’ interest to greatly reduce the number of false alarms. Working with scientists at the University Hospital Zurich’s Neurocritical Care Unit, researchers at ETH Zurich have now developed a machine learning method that aims to achieve just that.

## Computer does doctors’ legwork

As part of a feasibility study within a data science project called ICU Cockpit , the researchers made use of comprehensive intensive care data recordings. With the patients’ consent, their vital signs are systematically stored at high temporal resolution along with any alarms that may have sounded.

As is generally the case in ICUs, the various devices for circulatory monitoring, artificial ventilation and brain monitoring work independently of each other. Consequently, the devices each sound their own alarm whenever their readings go above or below a certain threshold value. The researchers combined and synchronised the data from these various devices and then applied novel machine learning techniques to identify which alarms were irrelevant from a medical standpoint.

## Works even with fragmentary data

“Usually, before a computer can start learning, humans first need to have categorised a certain number of alarms as relevant or non-relevant,” explains Walter Karlen, Professor of Mobile Health Systems at ETH Zurich. “Computer systems can then use this information to understand the principle behind the classification and ultimately categorise alarms themselves.”

However, having someone classify alarms in intensive care is a never-ending task, not only because it has to be done for each patient individually. Additionally, medical personnel treating patients in intensive care would not have the time to teach a computer as well.

## Reference

This means the ideal system for deployment in an ICU would be one that could teach itself even if nurses or doctors have classified only a small number of alarms. This is where the machine learning method that Karlen and his colleagues have developed really comes into its own.

The scientists tested their method using a small data set from the Zurich neurocritical care unit: records of the vital signs and alarms for 14 patients over a period of several days. On average, the medical devices sounded the alarm almost 700 times per patient per day; in other words, every two minutes. Although only 1,800 (13 percent) of the data set’s total of 14,000 alarms had been classified manually, the algorithm was nonetheless able to categorise the remaining alarms as real or false. If the scientists allowed for the system to have an error rate of 5 percent, it reduced the number of false alarms by 77 percent.

The scientists were also able to demonstrate that the method works even with a significantly lower degree of manual help: all it took was 25 or 50 manual classifications for the system to flag a large number of alarms as false. The scientists also showed that particularly in situations where there has been very little manual help, the new method is much more effective than existing machine learning methods.

This project analysed clinical data retrospectively. The researchers are now considering whether to study the effectiveness of their algorithm using a prospective clinical study.

Schwab P, Keller E, Muroi C, Mack DJ, Strässle C, Karlen W: Not to Cry Wolf: Distantly Supervised Multitask Learning in Critical Care . Proceedings of the 35th International Conference on Machine Learning, Stockholm, 2018

