package pengliu.me.backend.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.concurrent.ThreadLocalRandom;

@RestController
public class HelloController {

    @GetMapping("/api/hello")
    public String hello() {
        return "Hello, Prometheus and Micrometer!";
    }

    @GetMapping("/api/antoerhHello")
    public String anotherHello() {
        return "Another Hello, Prometheus and Micrometer!";
    }

    @GetMapping("/heavy")
    public String heavyTask() throws InterruptedException {
        // 模拟耗时任务
        try {
            // 生成一个介于 1000 到 5000 毫秒之间的随机值
            int sleepTime = ThreadLocalRandom.current().nextInt(1000, 5000);
            System.out.println("Sleeping for " + sleepTime + " milliseconds...");

            // 让线程休眠指定的时间
            Thread.sleep(sleepTime);

            System.out.println("Woke up after " + sleepTime + " milliseconds.");
        } catch (InterruptedException e) {
            System.err.println("Sleep was interrupted!");
            e.printStackTrace();
        }
        return "Heavy task completed!";
    }
}