package p3_dsbdal;

import java.io.IOException;
import java.util.HashSet;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Reducer;

public class MusicReducer
        extends Reducer<Text, Text, Text, Text>
{

    public void reduce(Text key,
                       Iterable<Text> values,
                       Context context)
            throws IOException, InterruptedException
    {

        HashSet<String> users = new HashSet<String>();

        int shareCount = 0;

        for (Text val : values)
        {

            String[] parts = val.toString().split(":");

            String user = parts[0];
            int shared = Integer.parseInt(parts[1]);

            users.add(user);

            if (shared == 1)
            {
                shareCount++;
            }
        }

        String result =
                "Listeners = " + users.size()
                + " , Shared Count = " + shareCount;

        context.write(
                key,
                new Text(result)
        );
    }
}