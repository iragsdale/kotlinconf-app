import UIKit
import KotlinConfAPI

let Conference = ConferenceService(context: ApplicationContext())

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?
    
    func applicationDidFinishLaunching(_ application: UIApplication) {
        UIApplication.shared.registerForRemoteNotifications()

        let center = UNUserNotificationCenter.current()
        if #available(iOS 12.0, *) {
            center.requestAuthorization(options: [.alert, .sound, .badge, .provisional]) { granted, error in
                if let error = error {
                    print("Could not request permission for notifications: \(error)")
                }
                else {
                    print("Granted perms: \(granted)")
                }
            }
        } else {
            print("Cannot request permissions")
        }

    }
    
    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        print("Registered for remote notifications: \(deviceToken.base64EncodedString())")
    }
    
    func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
        print("Failed to register for remote notifications: \(error)")
    }
}

