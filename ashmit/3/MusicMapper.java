package p3_dsbdal;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Mapper;

public class MusicMapper
        extends Mapper<LongWritable, Text, Text, Text>
{

    public void map(LongWritable key,
                    Text value,
                    Context context)
            throws IOException, InterruptedException
    {

        String line = value.toString();

        // skip header
        if (line.contains("UserId"))
        {
            return;
        }

        String[] data = line.split(",");

        if (data.length < 5)
        {
            return;
        }

        String userId = data[0];
        String trackId = data[1];
        String shared = data[2];

        // send trackId as key
        // userId:shared as value
        context.write(
                new Text(trackId),
                new Text(userId + ":" + shared)
        );
    }
}