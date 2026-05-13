package p1_dsbdal;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Mapper;

public class LogMapper extends Mapper<LongWritable, Text, Text, IntWritable>
{

    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException
    {

        String line = value.toString();

        String[] data = line.split(",");

        if (data.length < 8)
        {
            return;
        }

        String user = data[1];

        String login = data[5];
        String logout = data[7];

        String loginTimeStr = login.split(" ")[1];
        String logoutTimeStr = logout.split(" ")[1];

        String[] loginParts = loginTimeStr.split(":");
        String[] logoutParts = logoutTimeStr.split(":");

        int loginHour = Integer.parseInt(loginParts[0]);
        int loginMin = Integer.parseInt(loginParts[1]);

        int logoutHour = Integer.parseInt(logoutParts[0]);
        int logoutMin = Integer.parseInt(logoutParts[1]);

        int loginTime = loginHour * 60 + loginMin;
        int logoutTime = logoutHour * 60 + logoutMin;

        int duration = logoutTime - loginTime;

        context.write(new Text(user), new IntWritable(duration));
    }
}